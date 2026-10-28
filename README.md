# Lab 6: Calculator Build with PyBuilder

This is the graded PyBuilder exercise. The calculator implements addition,
subtraction, multiplication, division, modulus, exponentiation, and square root.
The unit tests cover all seven operations and invalid input for division,
modulus, and square root.

## Setup

From this directory:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Run the tests and build

```bash
.venv/bin/pyb run_unit_tests
.venv/bin/python -m unittest tests.unittest.calculator_Karim_Assi.test_calculator_Karim_Assi
.venv/bin/pyb publish
```

PyBuilder writes its output to `target/`; the distribution is under
`target/dist/`. The successful terminal build screenshot is in
`evidence/Build_Success_Screenshot.png`.
