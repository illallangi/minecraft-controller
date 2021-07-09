import kopf


PREFIX = "controllers.illallangi.enterprises"
COMPONENT = "application"
CRD_GROUP = "controllers.illallangi.enterprises"
CRD_VERSION = "v1"
CRD_SINGULAR = "minecraft"
CRD_PLURAL = "minecrafts"
LABEL_COMPONENT = "app.kubernetes.io/component"
LABEL_CONTROLLER = "app.kubernetes.io/controller"
LABEL_INSTANCE = "app.kubernetes.io/instance"
LABEL_NAME = "app.kubernetes.io/name"


@kopf.index(
    group=CRD_GROUP,
    version=CRD_VERSION,
    singular=CRD_SINGULAR,
)
def minecraft_idx(namespace, body, **_):
    return {
        namespace: {k: body[k] for k in body},
    }


@kopf.on.probe(id=minecraft_idx.__name__)
def minecraft_probe(minecraft_idx: kopf.Index, **_):
    return {namespace: list(minecraft_idx[namespace]) for namespace in minecraft_idx}
