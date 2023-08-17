import bash_colors


def do_print() -> None:
    sample_text = f"""
{bash_colors.BashColors.DARK_RED}hello {bash_colors.BashColors.LIGHT_BLUE}world{bash_colors.BashColors.RESET}

{bash_colors.BashColors.PAINT_GREEN_BOLD}Final result:{bash_colors.BashColors.RESET}
\tMichael - {bash_colors.BashColors.LIGHT_GRAY_STRIKE}DROPPED.{bash_colors.BashColors.RESET}
\tAngie   - {bash_colors.BashColors.LIGHT_RED_UNDERLINE}FAILED.{bash_colors.BashColors.RESET}
\tSam     - {bash_colors.BashColors.LIGHT_GREEN_BOLD}PASSED.{bash_colors.BashColors.RESET}
\tEdmond  - {bash_colors.BashColors.LIGHT_ORANGE_ITALIC}NEED MORE ROUNDS.{bash_colors.BashColors.RESET}
"""
    print("=========== with colors ===========")
    print(sample_text)

    print("========== without colors ==========")
    print(bash_colors.BashColors.remove_bash_color_code(sample_text))


if __name__ == "__main__":
    do_print()
