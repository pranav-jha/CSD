load CS16B019HalfAdder.hdl,
output-file CS16B019HalfAdder.out,
compare-to CS16B019HalfAdder.cmp,
output-list a%B3.1.3 b%B3.1.3 sum%B3.1.3 carry%B3.1.3;

set a 0,
set b 0,
eval,
output;

set a 0,
set b 1,
eval,
output;

set a 1,
set b 0,
eval,
output;

set a 1,
set b 1,
eval,
output;
