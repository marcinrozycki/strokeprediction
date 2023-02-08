"""
This is a boilerplate pipeline 'split_data'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=split_data, inputs="processed", outputs="splitted")])
