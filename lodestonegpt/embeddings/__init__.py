from lodestonegpt.embeddings.base import BaseEmbeddingProvider
from lodestonegpt.embeddings.openai_ import OpenAIEmbeddingProvider
from lodestonegpt.embeddings.azure_openai import AzureOpenAIEmbeddingProvider
from lodestonegpt.embeddings.hf import HuggingFaceEmbeddingProvider

user_providers = {}


def register_embedding_provider_type(provider):
    if isinstance(provider, BaseEmbeddingProvider):
        provider = provider.__class__
    if not isinstance(provider, type):
        raise TypeError(f"{provider} is not a class")
    if not issubclass(provider, BaseEmbeddingProvider):
        raise TypeError(f"{provider} does not inherit from BaseEmbeddingProvider")
    user_providers[provider.__name__] = provider


def from_config(config) -> BaseEmbeddingProvider:
    class_name = config["class"]
    clss = user_providers.get(class_name) or globals()[class_name]
    return clss.from_config(config)
