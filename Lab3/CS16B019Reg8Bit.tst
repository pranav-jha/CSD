

load CS16B019Reg8Bit.hdl,
output-file CS16B019Reg8Bit.out,
compare-to CS16B019Reg8Bit.cmp,
output-list time%S1.4.1 in%D1.6.1 load%B2.1.2 out%D1.6.1;

set in 0,
set load 0,
tick,
output;

tock,
output;

set in 0,
set load 1,
tick,
output;

tock,
output;

set in -32123,
set load 0,
tick,
output;

tock,
output;


set in -32123,
set load 1,
tick,
output;

tock,
output;

set in -32123,
set load 1,
tick,
output;

tock,
output;

set in -32123,
set load 0,
tick,
output;

tock,
output;



set in %B00010000,
set load 0,
tick,
output;

tock,
output;

set load 1,
tick,
output;

tock,
output;

set in %B00100000,
set load 0,
tick,
output;

tock,
output;

set load 1,
tick,
output;

tock,
output;

