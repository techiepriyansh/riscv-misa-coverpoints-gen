# riscv-misa-coverpoints-gen
Generates coverpoints for each of the relevant bits in the extension field of misa register given a valid RISC-V ISA string containing only ratified extensions.

## Usage
```bash
$ ./riscv_misa_covpt_gen.py <riscv-isa-string>
```
Example: [sample_run.txt](sample_run.txt)

## For Future Reference
[Notes](notes.md) list out a number of possible exceptions which may occur while testing the relevant coverpoints. These need to be taken care of while desining the tests and the trap handler.
