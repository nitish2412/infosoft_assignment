# Problem 3 - Debug Calendar Design
## Seps follow to debug the code
### 1. Issue: Overlapping Events Not Handled Properly
   The insert method in the Node class does not correctly check for overlaps between events. Overlap detection is essential to ensure that events do not overlap, as overlapping events are not allowed.
### 2. Incorrect Logic for Left and Right Insertion
  The recursive logic for inserting into the left or right subtree is inverted in the original code.
### 3. Edge Case Handling: Back-to-Back Events:
  The code does not correctly handle events that are back-to-back (e.g., [2, 3) and [3, 4) should not overlap).
