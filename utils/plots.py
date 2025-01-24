import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def lineplot_movingaverage_pattern(
    df: pd.DataFrame, var: str = "", filtval=None, avg_days: int = 1
) -> None:
    """
    Gráfico para visualizar patrones de demanda en el año para
    los registros que coincidan con el filtro construido a partir
    de var y fitval.
    La demanda es graficada en su media móvil para los días especificados
    en avg_days

    Parameters
    ----------
    df: Dataframe que se desea filtrar
    var: nombre de columna en df
    fitval: valor de la columna para filtrar

    Returns
    -------
    None

    """
    filt_df = df if filtval == "" else df[df[var] == filtval]
    filt_df.demanda = filt_df.demanda.rolling(avg_days).mean()
    plt.figure(figsize=(15, 6))
    sns.lineplot(x="month_day", y="demanda", hue="year", data=filt_df)
    plt.title(f"Lineplot month pattern for {var} == {filtval}")
    plt.xlabel("month_day")
    plt.ylabel("demanda")
    x_ticks = filt_df["month_day"].unique()[::avg_days]
    plt.xticks(x_ticks, rotation=45)
    plt.axvline(x="07-02", color='red', linestyle='--', linewidth=2)
    plt.grid()
    plt.show()


def barplot_month_pattern(df: pd.DataFrame, var: str = "", filtval=None) -> None:
    """
    Gráfico de barras que muestra las ventas totales por mes.

    Gráfico para visualizar patrones de demanda en el año para
    los registros que coincidan con el filtro construido a partir
    de var y fitval.
    

    Parameters
    ----------
    df: Dataframe que se desea filtrar
    var: nombre de columna en df
    fitval: valor de la columna para filtrar

    Returns
    -------
    None

    """
    filt_df = df if filtval == "" else df[df[var] == filtval]
    filt_df = filt_df[["month","year","demanda"]]
    filt_df = filt_df.groupby(["year","month"]).sum().reset_index()
    plt.figure(figsize=(15, 6))
    sns.barplot(x="month", y="demanda", hue="year", data=filt_df)
    plt.title(f"Lineplot month pattern for {var} == {filtval}")
    plt.xlabel("month")
    plt.ylabel("demanda")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()


def lineplot_weekday_pattern(df: pd.DataFrame, var: str = "", filtval=None) -> None:
    """
    Gráfico para visualizar patrones de demanda en la semana para
    los registros que coincidan con el filtro construido a partir
    de var y fitval

    Parameters
    ----------
    df: Dataframe que se desea filtrar
    var: nombre de columna en df
    fitval: valor de la columna para filtrar

    Returns
    -------
    None

    """
    filt_df = df if filtval == "" else df[df[var] == filtval]
    filt_df = filt_df[["month","day","demanda"]]
    filt_df = filt_df.groupby(["day","month"]).mean().reset_index()


    plt.figure(figsize=(15, 15))
    sns.lineplot(x="day", y="demanda", hue="month", data=filt_df,linewidth=3)
    plt.title(f"Lineplot week pattern for {var} == {filtval}")
    plt.xlabel("day")
    plt.ylabel("demanda")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
