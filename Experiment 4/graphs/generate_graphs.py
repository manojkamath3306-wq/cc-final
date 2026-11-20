from pathlib import Path

ROOT = Path(__file__).resolve().parent


def svg_bar_chart(title, subtitle, values, labels, x_label, y_label, color, width=760, height=420):
    max_value = max(values) if values else 1
    margin_left = 80
    margin_right = 30
    margin_top = 80
    margin_bottom = 80
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom
    bar_width = plot_width / (len(values) * 1.8)
    chart = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#f8fafc"/>',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="22" font-family="Arial, sans-serif" font-weight="700" fill="#0f172a">{title}</text>',
        f'<text x="{width/2}" y="54" text-anchor="middle" font-size="13" font-family="Arial, sans-serif" fill="#475569">{subtitle}</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#334155" stroke-width="1.5"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#334155" stroke-width="1.5"/>',
        f'<text x="{width/2}" y="{height-18}" text-anchor="middle" font-size="12" font-family="Arial, sans-serif" fill="#334155">{x_label}</text>',
        f'<text x="18" y="{height/2}" transform="rotate(-90 18 {height/2})" text-anchor="middle" font-size="12" font-family="Arial, sans-serif" fill="#334155">{y_label}</text>',
    ]

    grid_steps = 5
    for i in range(grid_steps + 1):
        y = margin_top + (plot_height * i / grid_steps)
        val = max_value * (1 - i / grid_steps)
        chart.append(f'<line x1="{margin_left}" y1="{y}" x2="{width-margin_right}" y2="{y}" stroke="#e2e8f0" stroke-width="1"/>')
        chart.append(f'<text x="{margin_left-12}" y="{y+4}" text-anchor="end" font-size="11" font-family="Arial, sans-serif" fill="#475569">{int(val)}</text>')

    for idx, val in enumerate(values):
        x = margin_left + idx * (plot_width / len(values)) + 18
        bar_h = (val / max_value) * plot_height
        y = height - margin_bottom - bar_h
        chart.append(f'<rect x="{x}" y="{y}" width="{bar_width}" height="{bar_h}" rx="8" fill="{color}" opacity="0.9"/>')
        chart.append(f'<text x="{x + bar_width/2}" y="{height-margin_bottom+18}" text-anchor="middle" font-size="11" font-family="Arial, sans-serif" fill="#334155">{labels[idx]}</text>')
        chart.append(f'<text x="{x + bar_width/2}" y="{y-8}" text-anchor="middle" font-size="11" font-family="Arial, sans-serif" fill="#0f172a">{val}</text>')

    chart.append('</svg>')
    return '\n'.join(chart)


def svg_grouped_bar_chart(title, subtitle, series, labels, x_label, y_label, width=760, height=420):
    max_value = max(max(v) for v in series.values()) if series else 1
    margin_left = 80
    margin_right = 30
    margin_top = 80
    margin_bottom = 80
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom
    group_width = plot_width / len(labels)
    bar_width = group_width / (len(series) + 2)
    chart = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#f8fafc"/>',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="22" font-family="Arial, sans-serif" font-weight="700" fill="#0f172a">{title}</text>',
        f'<text x="{width/2}" y="54" text-anchor="middle" font-size="13" font-family="Arial, sans-serif" fill="#475569">{subtitle}</text>',
        f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#334155" stroke-width="1.5"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#334155" stroke-width="1.5"/>',
        f'<text x="{width/2}" y="{height-18}" text-anchor="middle" font-size="12" font-family="Arial, sans-serif" fill="#334155">{x_label}</text>',
        f'<text x="18" y="{height/2}" transform="rotate(-90 18 {height/2})" text-anchor="middle" font-size="12" font-family="Arial, sans-serif" fill="#334155">{y_label}</text>',
    ]

    for i in range(6):
        y = margin_top + (plot_height * i / 5)
        chart.append(f'<line x1="{margin_left}" y1="{y}" x2="{width-margin_right}" y2="{y}" stroke="#e2e8f0" stroke-width="1"/>')
        val = max_value * (1 - i / 5)
        chart.append(f'<text x="{margin_left-12}" y="{y+4}" text-anchor="end" font-size="11" font-family="Arial, sans-serif" fill="#475569">{int(val)}</text>')

    colors = ['#2563eb', '#10b981', '#f59e0b']
    series_names = list(series.keys())
    for idx, label in enumerate(labels):
        x0 = margin_left + idx * group_width + 16
        for s_idx, s_name in enumerate(series_names):
            val = series[s_name][idx]
            x = x0 + s_idx * (bar_width + 10)
            bar_h = (val / max_value) * plot_height
            y = height - margin_bottom - bar_h
            chart.append(f'<rect x="{x}" y="{y}" width="{bar_width}" height="{bar_h}" rx="6" fill="{colors[s_idx]}" opacity="0.9"/>')
            chart.append(f'<text x="{x + bar_width/2}" y="{y-8}" text-anchor="middle" font-size="10" font-family="Arial, sans-serif" fill="#0f172a">{val}</text>')
        chart.append(f'<text x="{x0 + group_width/2 - 10}" y="{height-margin_bottom+18}" text-anchor="middle" font-size="11" font-family="Arial, sans-serif" fill="#334155">{label}</text>')

    legend_y = 68
    for i, s_name in enumerate(series_names):
        chart.append(f'<rect x="{width-200 + i*90}" y="{legend_y}" width="12" height="12" fill="{colors[i]}" rx="2"/>')
        chart.append(f'<text x="{width-182 + i*90}" y="{legend_y+11}" font-size="12" font-family="Arial, sans-serif" fill="#334155">{s_name}</text>')

    chart.append('</svg>')
    return '\n'.join(chart)


def svg_pie_chart(title, subtitle, values, labels, colors, width=600, height=420):
    total = sum(values)
    start = -90
    slices = []
    cx, cy, r = 210, 210, 120
    legend_x = 360
    legend_y = 150
    for val, label, color in zip(values, labels, colors):
        angle = (val / total) * 360 if total else 0
        end = start + angle
        x1 = cx + r * __import__('math').cos(__import__('math').radians(start))
        y1 = cy + r * __import__('math').sin(__import__('math').radians(start))
        x2 = cx + r * __import__('math').cos(__import__('math').radians(end))
        y2 = cy + r * __import__('math').sin(__import__('math').radians(end))
        large_arc = 1 if angle > 180 else 0
        path = f'M {cx} {cy} L {x1} {y1} A {r} {r} 0 {large_arc} 1 {x2} {y2} Z'
        slices.append(f'<path d="{path}" fill="{color}" stroke="#ffffff" stroke-width="2"/>')
        start = end

    chart = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#f8fafc"/>',
        f'<text x="{width/2}" y="32" text-anchor="middle" font-size="22" font-family="Arial, sans-serif" font-weight="700" fill="#0f172a">{title}</text>',
        f'<text x="{width/2}" y="56" text-anchor="middle" font-size="13" font-family="Arial, sans-serif" fill="#475569">{subtitle}</text>',
    ]
    chart.extend(slices)
    chart.append(f'<circle cx="{cx}" cy="{cy}" r="54" fill="#f8fafc"/>')
    chart.append(f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-size="30" font-family="Arial, sans-serif" font-weight="700" fill="#0f172a">{total}</text>')
    chart.append(f'<text x="{cx}" y="{cy+20}" text-anchor="middle" font-size="12" font-family="Arial, sans-serif" fill="#475569">requests</text>')
    for idx, (label, value, color) in enumerate(zip(labels, values, colors)):
        y = legend_y + idx * 28
        chart.append(f'<rect x="{legend_x}" y="{y-10}" width="12" height="12" fill="{color}" rx="2"/>')
        chart.append(f'<text x="{legend_x+20}" y="{y}" font-size="13" font-family="Arial, sans-serif" fill="#334155">{label}: {value}</text>')
    chart.append('</svg>')
    return '\n'.join(chart)


# Node resource snapshot from the experiment recording
node_cpu = [167, 34, 29]
node_mem = [710, 153, 135]
node_labels = ['Control-plane', 'Worker', 'Worker 2']

(ROOT / 'node-resource-usage.svg').write_text(
    svg_bar_chart(
        'Node CPU Usage',
        'Point-in-time sample from kubectl top nodes',
        node_cpu,
        node_labels,
        'Node',
        'CPU usage (m)',
        '#2563eb'
    )
)

(ROOT / 'node-memory-usage.svg').write_text(
    svg_bar_chart(
        'Node Memory Usage',
        'Point-in-time sample from kubectl top nodes',
        node_mem,
        node_labels,
        'Node',
        'Memory usage (Mi)',
        '#10b981'
    )
)

pod_series = {
    '6 replicas': [2, 2, 2],
    '12 replicas': [4, 4, 4],
}
(ROOT / 'pod-distribution.svg').write_text(
    svg_grouped_bar_chart(
        'Pod Distribution Across the 3 Nodes',
        'Observed placement after deployment and scale-out',
        pod_series,
        ['Control-plane', 'Worker', 'Worker 2'],
        'Node',
        'Pods placed',
    )
)

(ROOT / 'service-success.svg').write_text(
    svg_pie_chart(
        'HTTP Service Check',
        'Ten requests passed through the NodePort Service',
        [10, 0],
        ['Successful', 'Failed'],
        ['#10b981', '#ef4444'],
    )
)

(ROOT / 'README.md').write_text(
    """# Graphs for the Kubernetes Experiment

This folder contains a few concise comparison charts derived from the recorded experiment results.

## Included charts

- `node-resource-usage.svg` — CPU usage across the three nodes before scaling.
- `node-memory-usage.svg` — memory usage across the three nodes before scaling.
- `pod-distribution.svg` — pod placement comparison between 6 and 12 replicas.
- `service-success.svg` — success/failure breakdown for the HTTP checks through the NodePort Service.

## Interpretation

- The control-plane node carried the highest baseline CPU and memory load.
- The workload was spread evenly across all three nodes, with two pods per node at 6 replicas and four pods per node at 12 replicas.
- The service check showed 100% success rate for the tested HTTP requests.

These charts are intentionally simple and based on the observed values from the experiment recording and the lab documentation.
"""
)
