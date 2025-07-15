import pandas as pd

def matches_with_200_plus_scores():
    # Load datasets
    deliveries_df = pd.read_csv(r'D:\learning\deliveries.csv')
    matches_df = pd.read_csv(r'D:\learning\matches.csv')

    # Debugging: check available columns
    print("Deliveries columns:", deliveries_df.columns)
    print("Matches columns:", matches_df.columns)

    # Check for required columns
    required_deliveries_columns = {'match_id', 'batting_team', 'total_runs'}
    required_matches_columns = {'id', 'season', 'date', 'venue', 'winner'}

    if not required_deliveries_columns.issubset(deliveries_df.columns) or not required_matches_columns.issubset(matches_df.columns):
        print("One or more required columns are missing in the CSV files.")
        return

    # Group by match and batting team, then sum total_runs
    team_totals = deliveries_df.groupby(['match_id', 'batting_team'])['total_runs'].sum().reset_index()

    # Filter totals >= 200
    high_scoring = team_totals[team_totals['total_runs'] >= 200]

    # Merge with matches data to get extra context
    merged = pd.merge(high_scoring, matches_df, left_on='match_id', right_on='id')

    # Select relevant columns for display
    result = merged[['season', 'date', 'batting_team', 'total_runs', 'venue', 'winner']]

    # Sort by season and date
    result = result.sort_values(by=['season', 'date'])

    print("🏏 Matches where a team scored 200+ runs:\n")
    for _, row in result.iterrows():
        print(f"Season {row['season']} | {row['date']} | {row['batting_team']} scored {row['total_runs']} runs at {row['venue']} | Winner: {row['winner']}")

# Run the function
matches_with_200_plus_scores()
