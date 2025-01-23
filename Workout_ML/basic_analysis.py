import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/workout_history_cleaned.csv")
print(df.head())
print(df.info())


# Class Frequency Analysis
class_counts = df["class_name"].value_counts()
print("Class Frequencies:\n", class_counts)

plt.figure(figsize=(8, 6))
sns.barplot(x=class_counts.index, y=class_counts.values)
plt.title("Class Frequency")
plt.xlabel("Class Name")
plt.ylabel("Frequency")
plt.show()


# Time of Day Analysis


def convert_time_to_24hr(time_str):
    time_str = time_str.lower()  # Convert to lowercase for easier processing
    if "pm" in time_str:
        if time_str.startswith("12"):  # handle noon as a special case
            hour = 12
        else:
            hour = int(time_str.split(":")[0]) + 12
    else:
        hour = int(time_str.split(":")[0])
    minute = int(time_str.split(":")[1][:2])
    return hour + minute / 60


df["time_of_day_24hr"] = df["time_of_day"].apply(convert_time_to_24hr)

plt.figure(figsize=(10, 6))
sns.histplot(df["time_of_day_24hr"], bins=10, kde=True)
plt.title("Time of Day Distribution")
plt.xlabel("Time of Day (24 hour)")
plt.ylabel("Number of Classes")
plt.show()

# Duration Analysis
duration_stats = df["duration"].describe()
print("Duration Statistics:\n", duration_stats)

plt.figure(figsize=(8, 6))
sns.histplot(df["duration"], bins=5, kde=True)
plt.title("Class Duration Distribution")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Classes")
plt.show()
