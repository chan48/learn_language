import sys
sys.path.insert(0, "..")
from coderunner import test, Cpp, main

test(Cpp, "embed_output.cpp", is_file=True, is_embedded_output=True)

main()
