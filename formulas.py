def coefficient_correspondence(Q_ft_VVST, Q_mr_VVST):
    """
    Коэффициент соответствия наиболее значимых показателей.
    P_ВВСТ = Q_фтВВСТ / Q_мрВВСТ if Q_фтВВСТ < Q_мрВВСТ else 1
    """
    if Q_mr_VVST == 0:
        raise ValueError("Q_мрВВСТ не может быть нулем")
    if Q_ft_VVST < Q_mr_VVST:
        return Q_ft_VVST / Q_mr_VVST
    else:
        return 1.0

def provision_VVST_year(N_VVST, N_VVST_shtat):
    """
    Обеспеченность ВВСТ на год.
    P_ВВСТ = N_ВВСТ / N_ВВСТштат * 100% if N_ВВСТ <= N_ВВСТштат else 100%
    """
    if N_VVST_shtat == 0:
        raise ValueError("N_ВВСТштат не может быть нулем")
    if N_VVST <= N_VVST_shtat:
        return (N_VVST / N_VVST_shtat) * 100
    else:
        return 100.0

def provision_serviceable(N_isp_VVST, N_VVST_shtat):
    """
    Обеспеченность исправными образцами.
    P_осн.испр = N_испр.ВВСТ / N_ВВСТштат * 100% if N_испр.ВВСТ <= N_ВВСТштат else 100%
    """
    if N_VVST_shtat == 0:
        raise ValueError("N_ВВСТштат не может быть нулем")
    if N_isp_VVST <= N_VVST_shtat:
        return (N_isp_VVST / N_VVST_shtat) * 100
    else:
        return 100.0

def provision_modern(N_sovr_VVST, N_VVST_shtat):
    """
    Обеспеченность современными образцами ВВСТ.
    P_сов = N_совр.ВВСТ / N_ВВСТштат * 100% if N_совр.ВВСТ <= N_ВВСТштат else 100%
    """
    if N_VVST_shtat == 0:
        raise ValueError("N_ВВСТштат не может быть нулем")
    if N_sovr_VVST <= N_VVST_shtat:
        return (N_sovr_VVST / N_VVST_shtat) * 100
    else:
        return 100.0

def share_modern(N_sovr_VVST, N_VVST):
    """
    Доля современных образцов ВВСТ.
    P_сов.ВВСТ = N_совр.ВВСТ / N_ВВСТ * 100% if N_совр.ВВСТ <= N_ВВСТ else 100%
    """
    if N_VVST == 0:
        raise ValueError("N_ВВСТ не может быть нулем")
    if N_sovr_VVST <= N_VVST:
        return (N_sovr_VVST / N_VVST) * 100
    else:
        return 100.0

def technical_readiness(N_isp_VVST, N_VVST):
    """
    Коэффициент технической готовности ВВСТ.
    P_ктг = N_исп.ВВСТ / N_ВВСТ if N_исп.ВВСТ <= N_ВВСТ else 1
    """
    if N_VVST == 0:
        raise ValueError("N_ВВСТ не может быть нулем")
    if N_isp_VVST <= N_VVST:
        return N_isp_VVST / N_VVST
    else:
        return 1.0