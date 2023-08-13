source bash_colors.sh

echo "=========== with colors ==========="
text=$(cat <<EOF
${DARK_RED}hello ${LIGHT_BLUE}world${RESET}

${PAINT_GREEN_BOLD}Final result:${RESET}
\tMichael - ${LIGHT_GRAY_STRIKE}DROPPED.${RESET}
\tAngie   - ${LIGHT_RED_UNDERLINE}FAILED.${RESET}
\tSam     - ${LIGHT_GREEN_BOLD}PASSED.${RESET}
\tEdmond  - ${LIGHT_ORANGE_ITALIC}NEED MORE ROUNDS.${RESET}
EOF
)
echo "$text"

echo "========== without colors =========="
remove_bash_color_codes "$text"
echo "$result"