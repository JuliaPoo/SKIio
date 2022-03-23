from . import *
import argparse
import os


class SKIioCLIException(Exception):
    """Generic exception for CLI"""

    def __init__(self, message: str):
        message = f"[x] SKIioCLIException: {message}"
        super().__init__(message)


class SKIioCLIInternalException(Exception):
    """Generic exception for CLI that's pretty much my fault"""

    def __init__(self, message: str):
        message = f"[x] SKIioCLIInternalException: {message}"
        super().__init__(message)


parser = argparse.ArgumentParser(
    prog="SKIio",
    description="SKIio interpreter and compiler, command-line interface",
)

subparsers = parser.add_subparsers(dest="action", help="Action")

compile_args = subparsers.add_parser("compile", help="Compile Purr code", aliases=["c"])
compile_args.add_argument(
    "-i", "--infile", help="Input filename with Purr code", type=str, required=True
)
compile_args.add_argument(
    "-o",
    "--outfile",
    help="Output filename (without extension)",
    type=str,
    required=True,
)
compile_args.add_argument(
    "-opt",
    "--optimize",
    help="Toggle off optimization (default: %(default)s)",
    type=bool,
    default=True,
)
compile_args.add_argument(
    "-m",
    "--intermediate",
    help="Output intermediate representation (default: %(default)s)",
    type=bool,
    default=False,
)

run_args = subparsers.add_parser("run", help="Run SKIio code", aliases=["r"])
run_args.add_argument(
    "-i", "--infile", help="Input filename with SKIio code", type=str, required=True
)
run_args.add_argument(
    "-v",
    "--verbose",
    help="Prints debugging info (default: %(default)s)",
    action="store_true",
    default=None,
)
run_args.add_argument(
    "-vv",
    "--veryverbose",
    help="Steps through execution (default: %(default)s)",
    action="store_true",
    default=None,
)

args = parser.parse_args()


def main(args: argparse.Namespace) -> int:

    action = args.action

    if action in ["compile", "c"]:

        i, o, m, opt = args.infile, args.outfile, args.intermediate, args.optimize
        if not os.path.isfile(i):
            raise SKIioCLIException(f"Input file `infile={i}` does not exist!")
        i_code = open(i).read()

        if m:
            o += ".ipurr"

            try:
                m_code = compile_purr_to_node_str(i_code)
            except PurrCompileException as err:
                print(err)
                return 1

            open(o, "w").write(m_code)
            print(f"[*] Wrote output to `{o}` ^-^")
            return 0

        o += ".ski"

        try:
            f_code = compile_purr_to_ski_str(i_code, opt)
        except PurrCompileException as err:
            print(err)
            return 1

        open(o, "w").write(f_code)
        print(f"[*] Wrote output to `{o}` ^-^")
        return 0

    elif action in ["run", "r"]:

        i, dbg_level = args.infile, 2 if args.veryverbose else 1 if args.verbose else 0
        if not os.path.isfile(i):
            raise SKIioCLIException(f"Input file `infile={i}` does not exist!")
        i_code = open(i).read()

        print(f"---- PROGRAM START ----")
        try:
            ret = interpret_SKI_from_str(i_code, dbg_level)
        except SKIioInterpreterException as err:
            print(err)
            return 1
        except SKIioInternalException as err:
            print(err)
            print("[-] Did you input a .ski file?")
            return 1
        except KeyboardInterrupt as err:
            print("[x] Program terminated by user!")
            return 1
        print(f"\n----- PROGRAM END -----")
        print(f"\n[*] Return: {ret}")
        return 0

    raise SKIioCLIInternalException(f"Unknown action {action}")


exit(main(args))
