"""
مسئلهٔ تئوری مصرف‌کننده (اقتصاد خرد)

تابع مطلوبیت کاب-داگلاس:  U(x, y) = x^a * y^(1-a)   با a = 1/3
درآمد I = 120، قیمت‌ها Px = 2 و Py = 4، سپس Px به 1 کاهش می‌یابد.
"""

A = 1 / 3          # سهم مخارج کالای x
INCOME = 120
PY = 4
PX_OLD = 2
PX_NEW = 1


def utility(x, y, a=A):
    return x ** a * y ** (1 - a)


def marshallian_demand(px, py, income, a=A):
    """تقاضای مارشالی: x = aI/Px و y = (1-a)I/Py"""
    return a * income / px, (1 - a) * income / py


def mrs(x, y, a=A):
    """نرخ نهایی جانشینی MUx / MUy"""
    return (a / (1 - a)) * (y / x)


def expenditure(px, py, u, a=A):
    """تابع مخارج: کمترین درآمد لازم برای رسیدن به مطلوبیت u"""
    return u * (px / a) ** a * (py / (1 - a)) ** (1 - a)


def hicksian_demand_x(px, py, u, a=A):
    """تقاضای هیکسی (جبرانی) کالای x"""
    return a * expenditure(px, py, u, a) / px


def elasticities(px, py, income, a=A, h=1e-6):
    """کشش‌های قیمتی، درآمدی و متقاطع x به روش عددی"""
    x0 = marshallian_demand(px, py, income, a)[0]
    dx_dpx = (marshallian_demand(px + h, py, income, a)[0] - x0) / h
    dx_di = (marshallian_demand(px, py, income + h, a)[0] - x0) / h
    dx_dpy = (marshallian_demand(px, py + h, income, a)[0] - x0) / h
    return dx_dpx * px / x0, dx_di * income / x0, dx_dpy * py / x0


def main():
    # الف) سبد بهینه با قیمت‌های اولیه
    x0, y0 = marshallian_demand(PX_OLD, PY, INCOME)
    u0 = utility(x0, y0)
    print("الف) سبد بهینهٔ اولیه")
    print(f"    x = {x0:.2f}, y = {y0:.2f}, U = {u0:.2f}")

    # ب) شرط بهینگی MRS = Px/Py
    print("ب) شرط بهینگی")
    print(f"    MRS = {mrs(x0, y0):.4f}, Px/Py = {PX_OLD / PY:.4f}")

    # ج) کشش‌ها
    e_p, e_i, e_c = elasticities(PX_OLD, PY, INCOME)
    print("ج) کشش‌های تقاضای x")
    print(f"    قیمتی = {e_p:.3f}, درآمدی = {e_i:.3f}, متقاطع = {e_c:.3f}")

    # د) سبد بهینه پس از کاهش قیمت x
    x1, y1 = marshallian_demand(PX_NEW, PY, INCOME)
    u1 = utility(x1, y1)
    print("د) سبد بهینه پس از کاهش Px")
    print(f"    x = {x1:.2f}, y = {y1:.2f}, U = {u1:.2f}")

    # هـ) تجزیهٔ هیکس: اثر جانشینی و اثر درآمدی
    xh = hicksian_demand_x(PX_NEW, PY, u0)
    print("هـ) تجزیهٔ هیکس")
    print(f"    تقاضای هیکسی x = {xh:.2f}")
    print(f"    اثر جانشینی = {xh - x0:+.2f}")
    print(f"    اثر درآمدی  = {x1 - xh:+.2f}")
    print(f"    اثر کل      = {x1 - x0:+.2f}")

    # و) تغییر جبرانی و تغییر معادل
    cv = INCOME - expenditure(PX_NEW, PY, u0)
    ev = expenditure(PX_OLD, PY, u1) - INCOME
    print("و) سنجش رفاه")
    print(f"    CV = {cv:.2f}")
    print(f"    EV = {ev:.2f}")


if __name__ == "__main__":
    main()
