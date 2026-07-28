#!/usr/bin/env python3
"""
Split oversized code blocks in HLD markdown files so each block fits on one PDF page.
Splits at natural boundaries: blank lines, horizontal rules, or between box-drawing sections.
"""
import re
import os
import sys

HLD_DIR = "/Users/ajay.kumar/1notion/hld"
MAX_LINES = 52  # safe limit for one A4 page with margins + header/footer

def find_split_point(lines, start, end):
    """Find the best line to split a block, searching from the middle outward."""
    mid = (start + end) // 2
    best = None
    best_dist = float('inf')

    for i in range(start, end):
        line = lines[i].rstrip()
        dist = abs(i - mid)

        # Priority 1: completely blank lines inside the block
        if line == '' or line == '│' + ' ' * (len(line) - 1) + '│' if len(line) > 2 else False:
            if dist < best_dist:
                best = i
                best_dist = dist
                continue

        # Priority 2: lines that are just whitespace inside boxes
        stripped = line.strip().strip('│').strip()
        if stripped == '' and dist < best_dist:
            best = i
            best_dist = dist
            continue

        # Priority 3: horizontal separator lines (├───, └───, ╠═══, etc.)
        if re.match(r'^[\s│]*[├└╠╚┗┣┼─═┤┘╣╝┛┘]+[\s]*$', line):
            # Prefer splitting AFTER a bottom border (└, ╚, ┗)
            if any(c in line for c in '└╚┗┘╝┛'):
                if dist < best_dist:
                    best = i + 1  # split after the closing border
                    best_dist = dist
            # Or split BEFORE a top border that starts a new section (├)
            elif any(c in line for c in '├╠┣'):
                if dist < best_dist:
                    best = i
                    best_dist = dist

    # Priority 4: lines between closed and open boxes
    if best is None:
        for i in range(start, end - 1):
            curr = lines[i].rstrip()
            nxt = lines[i + 1].rstrip() if i + 1 < end else ''
            dist = abs(i - mid)
            # After a └ line followed by blank or ┌
            if ('└' in curr or '╚' in curr) and dist < best_dist:
                best = i + 1
                best_dist = dist

    # Fallback: split at the midpoint
    if best is None or best <= start or best >= end:
        best = mid

    return best


def split_block(block_lines):
    """Split a block into chunks of MAX_LINES or fewer."""
    if len(block_lines) <= MAX_LINES:
        return [block_lines]

    chunks = []
    remaining = block_lines[:]

    while len(remaining) > MAX_LINES:
        # Find split point within the first MAX_LINES lines
        split_at = find_split_point(remaining, MAX_LINES // 3, min(MAX_LINES - 2, len(remaining) - 5))

        if split_at <= 0 or split_at >= len(remaining):
            split_at = MAX_LINES - 2

        chunks.append(remaining[:split_at])
        remaining = remaining[split_at:]

    if remaining:
        chunks.append(remaining)

    return chunks


def process_file(filepath):
    with open(filepath) as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    i = 0
    modifications = 0

    while i < len(lines):
        line = lines[i]

        # Detect code block start
        if line.startswith('```'):
            lang = line[3:].strip()
            block_start = i
            i += 1
            block_lines = []

            # Collect block content
            while i < len(lines) and not lines[i].startswith('```'):
                block_lines.append(lines[i])
                i += 1

            if i < len(lines):
                # i is now at the closing ```
                if len(block_lines) > MAX_LINES:
                    # Split this block
                    chunks = split_block(block_lines)
                    modifications += 1

                    for ci, chunk in enumerate(chunks):
                        opener = f'```{lang}' if lang else '```'
                        new_lines.append(opener)
                        new_lines.extend(chunk)
                        new_lines.append('```')
                        if ci < len(chunks) - 1:
                            new_lines.append('')  # blank line between split blocks
                else:
                    # Keep as-is
                    new_lines.append(f'```{lang}' if lang else '```')
                    new_lines.extend(block_lines)
                    new_lines.append('```')

                i += 1  # skip closing ```
            else:
                # Unclosed block, keep as-is
                new_lines.append(f'```{lang}' if lang else '```')
                new_lines.extend(block_lines)
        else:
            new_lines.append(line)
            i += 1

    if modifications > 0:
        with open(filepath, 'w') as f:
            f.write('\n'.join(new_lines))
        print(f"  {os.path.basename(filepath)}: split {modifications} oversized blocks")
    else:
        print(f"  {os.path.basename(filepath)}: no changes needed")

    return modifications


def main():
    total = 0
    for fname in sorted(os.listdir(HLD_DIR)):
        if not fname.endswith('.md') or not fname[0].isdigit():
            continue
        total += process_file(os.path.join(HLD_DIR, fname))
    print(f"\nTotal: split {total} blocks across all files")


if __name__ == '__main__':
    main()
