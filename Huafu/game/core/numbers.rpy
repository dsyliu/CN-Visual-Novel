# core/numbers.rpy
# Chinese number helpers, shared by every grade.

init python:
    CN_NUM = ["", "一", "二", "三", "四", "五",
              "六", "七", "八", "九", "十"]

    def cn_num(k):
        """1 -> "一" ... 10 -> "十". Falls back to Arabic digits outside 0–10."""
        return CN_NUM[k] if 0 <= k < len(CN_NUM) else str(k)
