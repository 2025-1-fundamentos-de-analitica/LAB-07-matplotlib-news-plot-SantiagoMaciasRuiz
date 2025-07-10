"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import os
import pandas as pd
import matplotlib.pyplot as plt


def configure_plot_style():
    plt.style.use("seaborn-v0_8")
    plt.figure(figsize=(10, 6))
    plt.title("How people get their news", fontsize=16, pad=20)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)


def plot_media_trends(df, media, color, zorder, linewidth):
    plt.plot(df[media], color=color, zorder=zorder, linewidth=linewidth, label=media)
    annotate_data_points(df, media, color, zorder)


def annotate_data_points(df, media, color, zorder):
    first_year, last_year = df.index[0], df.index[-1]
    plt.scatter(first_year, df[media][first_year], color=color, zorder=zorder)
    plt.text(
        first_year - 0.2,
        df[media][first_year],
        f"{media} {df[media][first_year]}%",
        ha="right",
        va="center",
        color=color,
    )
    plt.scatter(last_year, df[media][last_year], color=color, zorder=zorder)
    plt.text(
        last_year + 0.2,
        df[media][last_year],
        f"{df[media][last_year]}%",
        ha="left",
        va="center",
        color=color,
    )


def save_plot(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    """Genera el gráfico de cómo las personas obtienen sus noticias."""
    df = pd.read_csv("files/input/news.csv", index_col=0)

    media_config = {
        "Television": {"color": "dimgray", "zorder": 1, "linewidth": 2},
        "Newspaper": {"color": "grey", "zorder": 1, "linewidth": 2},
        "Internet": {"color": "tab:blue", "zorder": 2, "linewidth": 4},
        "Radio": {"color": "lightgrey", "zorder": 1, "linewidth": 2},
    }

    configure_plot_style()

    for media, config in media_config.items():
        plot_media_trends(df, media, **config)

    plt.xticks(ticks=df.index, labels=df.index, ha="center")
    save_plot("files/plots/news.png")


pregunta_01()
