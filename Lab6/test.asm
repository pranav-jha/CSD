@32767 //last location in ROM
D=A //Stored in D register
@1
A=D+A //Increment the last location in Binary this would be a negative value
0;JMP //Overflow since the next cell doesn't exist
