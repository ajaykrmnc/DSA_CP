# Stack

Use stacks for LIFO simulation, expression parsing, and nearest-boundary problems. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Stack implementation | Build stack or basic operations | [Implement stack using array](<Stack implementation/Implement stack using array.md>), [Implement Stack using Linked List](<Stack implementation/Implement Stack using Linked List.md>), [Operations on Stack](<Stack implementation/Operations on Stack.md>), [Implement two stacks in an array](<Stack implementation/Implement two stacks in an array.md>) |
| Stack mutation | Delete middle, min-at-pop, duplicate removal | [Delete middle element of a stack](<Stack mutation/Delete middle element of a stack.md>), [Get min at pop](<Stack mutation/Get min at pop.md>), [Removing consecutive duplicates](<Stack mutation/Removing consecutive duplicates.md>), [Removing consecutive duplicates - 2](<Stack mutation/Removing consecutive duplicates - 2.md>) |
| Parentheses / expression parsing | Need matching brackets or infix/postfix conversion | [Parenthesis Checker](<Parentheses and expression parsing/Parenthesis Checker.md>), [Infix to Postfix](<Parentheses and expression parsing/Infix to Postfix.md>), [Evaluation of Postfix Expression](<Parentheses and expression parsing/Evaluation of Postfix Expression.md>) |
| Monotonic stack | Need next greater, stock span, histogram, max of min windows | [Next Greater Element](<Monotonic stack/Next Greater Element.md>), [Stock span problem](<Monotonic stack/Stock span problem.md>), [Maximum Rectangular Area in a Histogram](<Monotonic stack/Maximum Rectangular Area in a Histogram.md>), [Maximum of minimum for every window size](<Monotonic stack/Maximum of minimum for every window size.md>) |
| Elimination stack | Pairwise candidate elimination | [The Celebrity Problem](<Elimination stack/The Celebrity Problem.md>) |

## Pattern Matches

1. **Stack + monotonic boundary**: Next greater, stock span, histogram.
2. **Stack + parsing**: Parentheses, infix/postfix, postfix evaluation.
3. **Stack + auxiliary state**: Min stack variants.
4. **Stack + two pointers/matrix**: Celebrity candidate elimination.
