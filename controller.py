import kopf

import application
import presentation
import minecraft
import tls

__all__ = ["application", "presentation", "minecraft", "tls"]

PREFIX = "controllers.illallangi.enterprises"


@kopf.on.startup()
def configure(settings: kopf.OperatorSettings, **_):
    settings.persistence.progress_storage = kopf.AnnotationsProgressStorage(
        prefix=PREFIX
    )
    settings.persistence.diffbase_storage = kopf.AnnotationsDiffBaseStorage(
        prefix=PREFIX
    )
