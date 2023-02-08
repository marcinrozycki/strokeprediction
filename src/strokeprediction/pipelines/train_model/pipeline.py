"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=train_model, inputs="splitted", outputs="model")])
