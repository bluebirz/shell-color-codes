import shell_colors


def do_print() -> None:
    sample_text = f"""
{shell_colors.ShellColors.DARK_RED}hello {shell_colors.ShellColors.LIGHT_BLUE}world{shell_colors.ShellColors.RESET}

{shell_colors.ShellColors.PAINT_GREEN_BOLD}Final result:{shell_colors.ShellColors.RESET}
\tMichael - {shell_colors.ShellColors.LIGHT_GRAY_STRIKE}DROPPED.{shell_colors.ShellColors.RESET}
\tAngie   - {shell_colors.ShellColors.LIGHT_RED_UNDERLINE}FAILED.{shell_colors.ShellColors.RESET}
\tSam     - {shell_colors.ShellColors.LIGHT_GREEN_BOLD}PASSED.{shell_colors.ShellColors.RESET}
\tEdmond  - {shell_colors.ShellColors.LIGHT_ORANGE_ITALIC}NEED MORE ROUNDS.{shell_colors.ShellColors.RESET}
"""
    print("=========== with colors ===========")
    print(sample_text)

    print("========== without colors ==========")
    print(shell_colors.ShellColors.remove_shell_color_code(sample_text))


if __name__ == "__main__":
    do_print()
