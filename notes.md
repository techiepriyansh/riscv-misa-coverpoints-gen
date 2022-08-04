### Possible Exceptions (while testing the relevant coverpoints)
 * Writing misa may increase `IALIGN`, e.g., by disabling the “C” extension. If an instruction that would write `misa` increases `IALIGN`, and the subsequent instruction’s address is not `IALIGN`-bit aligned, then according to the specification, the write to `misa` should to suppressed. But a buggy implementation might throw an `INSTRUCTION_ADDRESS_MISALIGNED` fault.
 * An incomplete implementation which claims to implement some extensions but does not actually implement them might throw an `ILLEGAL_INSTRUCTION` fault.
 * `ILLEGAL_INSTRUCTION` faults may also happen if the implementation does not properly handle the case of writing unsupported combinations of the extension bits.
