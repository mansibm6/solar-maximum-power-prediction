"""Reusable experiment functions extracted from MPPT_Prediction.ipynb."""

from __future__ import annotations


def build_model_1_cell_10():
    """Build the original architecture without training or accessing data."""
    import tensorflow as tf

    return tf.keras.Sequential(
        [
            tf.keras.layers.Dense(100, activation="relu"),
            tf.keras.layers.Dense(10, activation="relu"),
            tf.keras.layers.Dense(1),
        ]
    )


def build_model_2_cell_22():
    """Build the original architecture without training or accessing data."""
    import tensorflow as tf

    return tf.keras.Sequential(
        [
            tf.keras.layers.Dense(100, activation="relu"),
            tf.keras.layers.Dense(100, activation="relu"),
            tf.keras.layers.Dense(1),
        ]
    )
