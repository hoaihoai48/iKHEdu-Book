// Solution Scratchblocks DSL for sca_pen_p14: 8-Petal Rainbow Flower
define ve_cung_tron (goc) (buoc)
repeat (goc)
    move (buoc) steps
    turn right (1) degrees
end

define ve_canh_hoa (buoc)
repeat (2)
    ve_cung_tron (90) (buoc)
    turn right (90) degrees
end

when green flag clicked
erase all
pen up
go to x: (0) y: (0)
point in direction (0)
set pen size to (3)
set pen color to [#ff0000]
pen down

repeat (8)
    ve_canh_hoa (1.2)
    change pen color by (15)
    turn right (45) degrees
end

hide
