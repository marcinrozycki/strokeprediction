"""
This is a boilerplate pipeline 'preprocess'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import encode_data, fill_na


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=fill_na, inputs="input_data", outputs="temp"),
                     node(func=encode_data, inputs="temp", outputs="processed")])
