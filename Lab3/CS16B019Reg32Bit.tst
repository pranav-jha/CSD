

load CS16B019Reg32Bit.hdl,
output-file CS16B019Reg32Bit.out,
//compare-to CS16B019Reg32Bit.cmp,
output-list time%S1.4.1 in%D1.6.1 load%B2.1.2 out%D1.6.1;

set in 0,
set in1 0,
set load 0,
tick,
output;

tock,
output;

set in 0,
set in1 1,
set load 1,
tick,
output;

tock,
output;

set in -32123,
set in1 -32123,
set load 1,
tick,
output;

tock,
output;


set in -32123,
set in1 12345,
set load 0,
tick,
output;

tock,
output;




