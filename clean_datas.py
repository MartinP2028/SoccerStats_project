import pandas as pd # type: ignore

# Read stats_players.csv
df_stats = pd.read_csv('ressources/stats_players.csv', sep=';')

# Rename columns
df_stats = df_stats.rename(columns={"Playing Time_MP": "total_match_played", "Playing Time_Starts":"total_match_started", "Nation_Alpha3": "nation_geo_code"})

# New columns
df_stats['avg_goal_per_match'] = df_stats['Performance_Gls'] / df_stats['total_match_played']
df_stats['avg_assist_per_match'] = df_stats['Performance_Ast'] / df_stats['total_match_played']

# Round values
df_stats['avg_goal_per_match'] = df_stats['avg_goal_per_match'].round(2)
df_stats['avg_assist_per_match'] = df_stats['avg_assist_per_match'].round(2)

# Save final DataFrame to CSV
print(df_stats.head())
output_file = "cleaned_stats_players_top5.csv"
df_stats.to_csv(output_file, index=False)
print(f"Successfully saved final dataframe to {output_file}")
