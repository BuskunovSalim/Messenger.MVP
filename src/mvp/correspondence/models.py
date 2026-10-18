from dataclasses import dataclass

@dataclass(slots=True)
class CreateCorrespondenceRequest:
    ...

@dataclass(slots=True)
class CreateCorrespondenceResponse:
    ...

@dataclass(slots=True)
class SendMessageRequest:
    ...

@dataclass(slots=True)
class SendMessageResponse:
    ...

@dataclass(slots=True)
class GetCorrespondenceRequest:
    ...

@dataclass(slots=True)
class GetCorrespondenceResponse:
    ...
