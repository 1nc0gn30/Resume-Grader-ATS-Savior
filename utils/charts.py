import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_pie_chart(data):
    labels = ["Green", "Yellow", "Red"]
    counts = {"Green": 0, "Yellow": 0, "Red": 0}

    for r in data:
        try:
            score = int(r[4])
        except (TypeError, ValueError):
            continue
        if score >= 80:
            counts["Green"] += 1
        elif score >= 60:
            counts["Yellow"] += 1
        else:
            counts["Red"] += 1

    # Filter out labels with 0 count
    filtered = [(label, count) for label, count in counts.items() if count > 0]
    if not filtered:
        return plt.figure()  # Empty placeholder if no data

    labels, sizes = zip(*filtered)

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        colors=["#22c55e", "#eab308", "#ef4444"][:len(labels)],
        startangle=140,
        textprops=dict(color="white"),
        shadow=True
    )
    ax.set_title("Grade Distribution", color="white", fontsize=14)
    fig.patch.set_facecolor('#111')
    ax.set_facecolor('#111')

    return fig

def plot_score_trend(data):
    scores = []
    for r in data:
        try:
            score = int(r[4])
            scores.append(score)
        except (TypeError, ValueError):
            continue

    submissions = list(range(1, len(scores) + 1))
    if not scores:
        return plt.figure()  # Return empty if no scores

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(submissions, scores, marker='o', color="#0ea5e9", linewidth=2)
    ax.set_title("Resume Scores Over Time", color="white", fontsize=14)
    ax.set_xlabel("Submission #", color="white")
    ax.set_ylabel("Score", color="white")
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.grid(True, linestyle='--', alpha=0.4)

    fig.patch.set_facecolor('#111')
    ax.set_facecolor('#111')
    ax.tick_params(colors='white')

    return fig
