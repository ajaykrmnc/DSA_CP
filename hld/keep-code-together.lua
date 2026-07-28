-- Pandoc Lua filter: wrap code blocks in a minipage to prevent page breaks
function CodeBlock(block)
  local code = block.text
  local raw_before = pandoc.RawBlock('latex', '\\begin{minipage}{\\linewidth}')
  local raw_after = pandoc.RawBlock('latex', '\\end{minipage}\\vspace{0.5em}')
  return {raw_before, block, raw_after}
end
