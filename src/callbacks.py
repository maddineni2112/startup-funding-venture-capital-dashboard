# callbacks.py

from dash import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

from data import df


def register_callbacks(app):

    # ------------------------------------------------------------------
    # DASHBOARD 1
    # ------------------------------------------------------------------
    @app.callback(
        Output("country-bar", "figure"),
        Output("top-cities-bar", "figure"),
        Output("stage-bar", "figure"),
        Input("year-range-1", "value"),
        Input("industry-dropdown-1", "value"),
    )
    def update_dashboard1(year_range, industry_value):
        year_low, year_high = year_range

        mask_year = df["founding_year"].between(year_low, year_high)
        if industry_value == "ALL":
            mask_industry = df["major_industry"].notna()
        else:
            mask_industry = df["major_industry"] == industry_value

        df_filtered = df.loc[mask_year & mask_industry].copy()

        # ----- Top countries -----
        if df_filtered.empty:
            country_fig = px.bar(title="No countries for selected filters")
            country_fig.update_layout(template="plotly_dark", height=600, autosize=False)
        else:
            country_group = (
                df_filtered.dropna(subset=["country_code"])
                .groupby("country_code", as_index=False)["funding_total_usd"]
                .sum()
                .sort_values("funding_total_usd", ascending=False)
                .head(15)
            )
            country_fig = px.bar(
                country_group,
                x="funding_total_usd",
                y="country_code",
                orientation="h",
                labels={
                    "funding_total_usd": "Total funding (USD)",
                    "country_code": "Country",
                },
            )
            country_fig.update_layout(
                template="plotly_dark",
                yaxis=dict(autorange="reversed"),
                margin=dict(l=80, r=20, t=20, b=40),
                height=600,
                autosize=False,
            )

        # ----- Top cities -----
        if df_filtered.empty:
            cities_fig = px.bar(title="No cities for selected filters")
            cities_fig.update_layout(template="plotly_dark", height=350, autosize=False)
        else:
            city_group = (
                df_filtered.dropna(subset=["city"])
                .groupby("city", as_index=False)["funding_total_usd"]
                .sum()
                .sort_values("funding_total_usd", ascending=False)
                .head(10)
            )
            cities_fig = px.bar(
                city_group,
                x="funding_total_usd",
                y="city",
                orientation="h",
                labels={
                    "funding_total_usd": "Total funding (USD)",
                    "city": "City",
                },
            )
            cities_fig.update_layout(
                template="plotly_dark",
                yaxis=dict(autorange="reversed"),
                height=350,
                autosize=False,
            )

        # ----- Funding by stage -----
        stage_cols = [
            "funding_seed",
            "funding_a",
            "funding_b",
            "funding_c",
            "funding_angel",
            "funding_debt_round",
        ]
        stage_labels = {
            "funding_seed": "Seed",
            "funding_a": "Series A",
            "funding_b": "Series B",
            "funding_c": "Series C",
            "funding_angel": "Angel",
            "funding_debt_round": "Debt",
        }

        if df_filtered.empty:
            stage_fig = px.bar(title="No funding stages for selected filters")
            stage_fig.update_layout(template="plotly_dark", height=300, autosize=False)
        else:
            totals = {
                stage_labels[col]: df_filtered[col].sum(skipna=True)
                for col in stage_cols
                if col in df_filtered
            }
            stage_names = list(totals.keys())
            stage_values = list(totals.values())

            stage_fig = px.bar(
                x=stage_names,
                y=stage_values,
                labels={"x": "Funding stage", "y": "Total amount (USD)"},
            )
            stage_fig.update_layout(
                template="plotly_dark",
                height=300,
                autosize=False,
            )

        return country_fig, cities_fig, stage_fig

    # ------------------------------------------------------------------
    # DASHBOARD 2
    # ------------------------------------------------------------------
    @app.callback(
        Output("funding-line", "figure"),
        Output("count-line", "figure"),
        Output("industry-bar", "figure"),
        Output("industry-pie", "figure"),
        Input("year-range-2", "value"),
        Input("industry-dropdown-2", "value"),
    )
    def update_dashboard2(year_range, industry_value):
        year_low, year_high = year_range

        mask_year = df["founding_year"].between(year_low, year_high)
        if industry_value == "ALL":
            mask_industry = df["major_industry"].notna()
        else:
            mask_industry = df["major_industry"] == industry_value

        df_time = df.loc[mask_year & mask_industry].copy()
        df_industry = df.loc[mask_year].copy()

        # ----- Total funding per year -----
        if df_time.empty:
            funding_line = px.line(title="No data for selected filters")
            funding_line.update_layout(template="plotly_dark", height=320, autosize=False)
        else:
            funding_by_year = (
                df_time.dropna(subset=["founding_year"])
                .groupby("founding_year", as_index=False)["funding_total_usd"]
                .sum()
                .sort_values("founding_year")
            )
            funding_line = px.line(
                funding_by_year,
                x="founding_year",
                y="funding_total_usd",
                labels={
                    "founding_year": "Founding year",
                    "funding_total_usd": "Total funding (USD)",
                },
            )
            funding_line.update_layout(
                template="plotly_dark",
                height=320,
                autosize=False,
            )

        # ----- Number of funded startups per year -----
        if df_time.empty:
            count_line = px.line(title="No data for selected filters")
            count_line.update_layout(template="plotly_dark", height=320, autosize=False)
        else:
            count_by_year = (
                df_time.dropna(subset=["founding_year"])
                .groupby("founding_year", as_index=False)
                .size()
                .rename(columns={"size": "startup_count"})
                .sort_values("founding_year")
            )
            count_line = px.line(
                count_by_year,
                x="founding_year",
                y="startup_count",
                labels={
                    "founding_year": "Founding year",
                    "startup_count": "Number of funded startups",
                },
            )
            count_line.update_layout(
                template="plotly_dark",
                height=320,
                autosize=False,
            )

        # ----- Industry bar & pie -----
        if df_industry.empty:
            industry_bar = px.bar(title="No industries for selected filters")
            industry_bar.update_layout(template="plotly_dark", height=320, autosize=False)
            industry_pie = px.pie(title="No industries for selected filters")
            industry_pie.update_layout(template="plotly_dark", height=320, autosize=False)
        else:
            industry_group = (
                df_industry.dropna(subset=["major_industry"])
                .groupby("major_industry", as_index=False)["funding_total_usd"]
                .sum()
                .sort_values("funding_total_usd", ascending=False)
            )
            top10_ind = industry_group.head(10)

            industry_bar = px.bar(
                top10_ind,
                x="funding_total_usd",
                y="major_industry",
                orientation="h",
                labels={
                    "funding_total_usd": "Total funding (USD)",
                    "major_industry": "Industry",
                },
            )
            industry_bar.update_layout(
                template="plotly_dark",
                yaxis=dict(autorange="reversed"),
                margin=dict(l=120, r=20, t=20, b=40),
                height=320,
                autosize=False,
            )

            industry_pie = px.pie(
                top10_ind,
                names="major_industry",
                values="funding_total_usd",
                hole=0.3,
            )
            industry_pie.update_layout(
                template="plotly_dark",
                height=320,
                autosize=False,
            )

        return funding_line, count_line, industry_bar, industry_pie

    # ------------------------------------------------------------------
    # SHEET 1 – Line chart: # startups per year
    # ------------------------------------------------------------------
    @app.callback(
        Output("sheet1-year-line", "figure"),
        Input("sheet1-year-range", "value"),
    )
    def update_sheet1_year_line(year_range):
        year_low, year_high = year_range

        mask_year = df["founding_year"].between(year_low, year_high)
        df_time = df.loc[mask_year].dropna(subset=["founding_year"]).copy()

        if df_time.empty:
            fig = px.line(title="No data for selected year range")
            fig.update_layout(
                template="plotly_dark",
                height=220,
                margin=dict(l=40, r=20, t=30, b=40),
            )
            return fig

        year_group = (
            df_time.groupby("founding_year", as_index=False)
            .size()
            .rename(columns={"size": "startup_count"})
            .sort_values("founding_year")
        )

        fig = px.line(
            year_group,
            x="founding_year",
            y="startup_count",
            labels={
                "founding_year": "Founding year",
                "startup_count": "Number of startups founded",
            },
        )
        fig.update_layout(
            template="plotly_dark",
            height=220,
            margin=dict(l=40, r=20, t=30, b=40),
        )
        return fig

    # ------------------------------------------------------------------
    # SHEET 2 – Pie charts by funding stage & industry
    # ------------------------------------------------------------------
    @app.callback(
        Output("sheet2-pie-count", "figure"),
        Output("sheet2-pie-sum", "figure"),
        Input("sheet2-industry-dropdown", "value"),
    )
    def update_sheet2_pies(industry_value):
        # Filter by industry (or all)
        if industry_value == "ALL":
            dff = df.copy()
        else:
            dff = df[df["major_industry"] == industry_value].copy()

        # Define stage columns
        stage_cols = {
            "Seed": "funding_seed",
            "Series A": "funding_a",
            "Series B": "funding_b",
            "Series C": "funding_c",
            "Angel": "funding_angel",
            "Debt / Other": "funding_debt_round",
        }

        # Prepare counts and sums
        counts = {}
        sums = {}
        for label, col in stage_cols.items():
            if col in dff.columns:
                col_vals = dff[col].fillna(0)
                counts[label] = (col_vals > 0).sum()
                sums[label] = col_vals.sum()
            else:
                counts[label] = 0
                sums[label] = 0.0

        # Pie chart: counts
        pie_count = px.pie(
            names=list(counts.keys()),
            values=list(counts.values()),
            hole=0.3,
            title="Share of startups by funding stage",
        )
        pie_count.update_layout(
            template="plotly_dark",
            margin=dict(l=10, r=10, t=40, b=10),
            legend_title_text="Funding stage",
        )

        # Pie chart: sums
        pie_sum = px.pie(
            names=list(sums.keys()),
            values=list(sums.values()),
            hole=0.3,
            title="Share of total capital by funding stage",
        )
        pie_sum.update_layout(
            template="plotly_dark",
            margin=dict(l=10, r=10, t=40, b=10),
            legend_title_text="Funding stage",
        )

        return pie_count, pie_sum

    # ------------------------------------------------------------------
    # SHEET 2 – Combo bar + line over founding year
    # ------------------------------------------------------------------
    @app.callback(
        Output("sheet2-combo", "figure"),
        Input("sheet2-series-dropdown", "value"),
    )
    def update_sheet2_combo(selected_series_col):
        # Human-readable label for the title
        label_map = {
            "funding_seed": "Seed",
            "funding_a": "Series A",
            "funding_b": "Series B",
            "funding_c": "Series C",
            "funding_angel": "Angel",
            "funding_debt_round": "Debt / Other",
        }
        stage_label = label_map.get(selected_series_col, selected_series_col)

        # 1) Keep only rows with a founding year
        dff = df.dropna(subset=["founding_year"]).copy()

        # 2) Make sure founding_year is numeric and integer
        dff["founding_year"] = pd.to_numeric(dff["founding_year"], errors="coerce")
        dff = dff.dropna(subset=["founding_year"])
        if dff.empty:
            fig = go.Figure()
            fig.update_layout(
                template="simple_white",
                title="No founding year data",
                height=280,
            )
            return fig

        dff["founding_year"] = dff["founding_year"].astype(int)

        # 3) Check that the selected funding series exists
        if selected_series_col not in dff.columns:
            fig = go.Figure()
            fig.update_layout(
                template="simple_white",
                title=f"No data column for {stage_label}",
                height=280,
            )
            return fig

        # 4) Extract the stage amount and filter positives
        dff["stage_amount"] = pd.to_numeric(
            dff[selected_series_col], errors="coerce"
        ).fillna(0)

        dff_pos = dff[dff["stage_amount"] > 0].copy()
        if dff_pos.empty:
            fig = go.Figure()
            fig.update_layout(
                template="simple_white",
                title=f"No positive funding values for {stage_label}",
                height=280,
            )
            return fig

        # 5) Group by founding_year: count rows and sum funding
        grouped = (
            dff_pos.groupby("founding_year")
            .agg(
                startup_count=("stage_amount", "size"),
                total_amount=("stage_amount", "sum"),
            )
            .reset_index()
            .sort_values("founding_year")
        )

        # 6) Build combo chart with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Bars: count of startups (left axis)
        fig.add_trace(
            go.Bar(
                x=grouped["founding_year"],
                y=grouped["startup_count"],
                name="Number of startups",
                marker_color="#1f77b4",
            ),
            secondary_y=False,
        )

        # Line: total funding amount (right axis)
        fig.add_trace(
            go.Scatter(
                x=grouped["founding_year"],
                y=grouped["total_amount"],
                name="Total funding (USD)",
                mode="lines+markers",
                line=dict(color="red", width=2),
            ),
            secondary_y=True,
        )

        fig.update_layout(
            template="simple_white",  # white like Tableau
            height=280,
            margin=dict(l=50, r=60, t=40, b=40),
            title=f"{stage_label} funding over founding years",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
            ),
        )

        fig.update_xaxes(title_text="Year of founding")
        fig.update_yaxes(
            title_text="Count of startups",
            secondary_y=False,
        )
        fig.update_yaxes(
            title_text=f"{stage_label} funding (USD)",
            secondary_y=True,
        )

        return fig
    # ------------------------------------------------------------------
    # SHEET 3 – Choropleth + Scatter Map (Interactive by Industry Filter)
    # ------------------------------------------------------------------
    @app.callback(
        Output("sheet3-choropleth", "figure"),
        Output("sheet3-scatter", "figure"),
        Input("sheet3-industry-filter", "value")
    )
    def update_sheet3_maps(selected_industry):

        # --- Filter dataset ---
        if selected_industry == "ALL":
            dff = df.copy()
        else:
            dff = df[df["major_industry"] == selected_industry].copy()

        # ===============================
        # 1) Choropleth (Country Funding)
        # ===============================
        country_group = (
            dff.dropna(subset=["country_code"])
            .groupby("country_code", as_index=False)["funding_total_usd"]
            .sum()
        )

        choropleth_fig = px.choropleth(
            country_group,
            locations="country_code",
            locationmode="ISO-3",
            color="funding_total_usd",
            color_continuous_scale="Viridis",
            range_color=(0, 1e10),
            title="Total Funding by Country",
        )

        choropleth_fig.update_layout(
            height=320,
            margin=dict(l=0, r=0, t=30, b=0),
        )

        # ===============================
        # 2) Flat Scatter Map (Industry)
        # ===============================
        dff_points = dff.dropna(subset=["latitude", "longitude"])

        scatter_fig = px.scatter_mapbox(
            dff_points,
            lat="latitude",
            lon="longitude",
            color="major_industry",
            hover_name="city",
            hover_data={"country_code": True},
            zoom=1,
            height=360,
        )

        scatter_fig.update_layout(
            mapbox_style="open-street-map",   # flat rectangular map
            margin=dict(l=0, r=0, t=0, b=0),
            legend_title="Major Industry",
        )

        scatter_fig.update_traces(marker=dict(size=5, opacity=0.85))

        return choropleth_fig, scatter_fig
