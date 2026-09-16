// Solution Scratchblocks DSL for sca_pen_p12: Olympic 5 Rings
define ve_hinh_tron (buoc)
repeat (360)
    move (buoc) steps
    turn right (1) degrees
end

when green flag clicked
erase all
pen up
set pen size to (6)

// Ring 1: Blue
go to x: (-110) y: (40)
point in direction (90)
set pen color to [#0085C7]
pen down
ve_hinh_tron (0.7)
pen up

// Ring 2: Black
go to x: (-30) y: (40)
point in direction (90)
set pen color to [#000000]
pen down
ve_hinh_tron (0.7)
pen up

// Ring 3: Red
go to x: (50) y: (40)
point in direction (90)
set pen color to [#DF0024]
pen down
ve_hinh_tron (0.7)
pen up

// Ring 4: Yellow
go to x: (-70) y: (0)
point in direction (90)
set pen color to [#F4C300]
pen down
ve_hinh_tron (0.7)
pen up

// Ring 5: Green
go to x: (10) y: (0)
point in direction (90)
set pen color to [#009F3D]
pen down
ve_hinh_tron (0.7)
pen up

hide
