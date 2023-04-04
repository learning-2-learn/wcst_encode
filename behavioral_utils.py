from constants import FEATURES
import numpy as np
import pandas as pd

def get_X_by_bins(bin_size, data):
    """
    bin_size: in miliseconds, bin size
    data: dataframe for behavioral data from object features csv
    Returns: new dataframe with one-hot encoding of features, feedback
    """
    max_time = np.max(data["TrialEnd"].values)
    max_bin_idx = int(max_time / bin_size) + 1
    columns = FEATURES + ["CORRECT", "INCORRECT"]
    types = ["f4" for _ in columns]
    zipped = list(zip(columns, types))
    dtype = np.dtype(zipped)
    arr = np.zeros((max_bin_idx), dtype=dtype)

    for _, row in data.iterrows():
        # grab features of item chosen
        item_chosen = int(row["ItemChosen"])
        color = row[f"Item{item_chosen}Color"]
        shape = row[f"Item{item_chosen}Shape"]
        pattern = row[f"Item{item_chosen}Pattern"]

        chosen_time = row["FeedbackOnset"] - 800
        chosen_bin = int(chosen_time / bin_size)
        arr[chosen_bin][color] = 1
        arr[chosen_bin][shape] = 1
        arr[chosen_bin][pattern] = 1

        feedback_bin = int(row["FeedbackOnset"] / bin_size)
        # print(feedback_bin)
        if row["Response"] == "Correct":
            arr[feedback_bin]["CORRECT"] = 1
        else:
            arr[feedback_bin]["INCORRECT"] = 1
    df = pd.DataFrame(arr)
    df["bin_idx"] = np.arange(len(df))
    return df


def get_trial_intervals(behavioral_data, event="FeedbackOnset", pre_interval=0, post_interval=0, bin_size=50):
    """Per trial, finds time interval surrounding some event in the behavioral data

    Args:
        behavioral_data: Dataframe describing each trial, must contain
            columns: TrialNumber, whatever 'event' param describes
        event: name of event to align around, must be present as a
            column name in behavioral_data Dataframe
        pre_interval: number of miliseconds before event
        post_interval: number of miliseconds after event

    Returns:
        DataFrame with num_trials length, columns: TrialNumber,
        IntervalStartTime, IntervalEndTime
    """
    trial_event_times = behavioral_data[["TrialNumber", event]]

    intervals = np.empty((len(trial_event_times), 3))
    intervals[:, 0] = trial_event_times["TrialNumber"]
    intervals[:, 1] = trial_event_times[event] - pre_interval
    intervals[:, 2] = trial_event_times[event] + post_interval
    intervals_df = pd.DataFrame(columns=["TrialNumber", "IntervalStartTime", "IntervalEndTime"])
    intervals_df["TrialNumber"] = trial_event_times["TrialNumber"].astype(int)
    intervals_df["IntervalStartTime"] = trial_event_times[event] - pre_interval
    intervals_df["IntervalEndTime"] = trial_event_times[event] + post_interval
    intervals_df["IntervalStartBin"] = (intervals_df["IntervalStartTime"] / bin_size).astype(int)
    intervals_df["IntervalEndBin"] = (intervals_df["IntervalEndTime"] / bin_size).astype(int)
    return intervals_df