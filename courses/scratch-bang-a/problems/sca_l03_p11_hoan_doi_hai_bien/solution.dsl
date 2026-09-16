// Solution Scratchblocks DSL for sca_l03_p11: Swap Two Variables
when green flag clicked
ask [Nhap so A:] and wait
set [A v] to (answer)
ask [Nhap so B:] and wait
set [B v] to (answer)

// Swap algorithm using temporary variable tam
set [tam v] to (A)
set [A v] to (B)
set [B v] to (tam)

// Output with space separation
say (join (A) (join [ ] (B)))
