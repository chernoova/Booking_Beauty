from abc import ABC, abstractmethod
from typing import Type

import src.repositories as repositories


class AbstractUnitOfWork(ABC):
    user: Type[repositories.user_repository.UserRepository]
    service: Type[repositories.service_repository.ServiceRepository]
    specialist: Type[repositories.specialist_repository.SpecialistRepository]
    appointment: Type[repositories.appointment_repository.AppointmentRepository]
    beauty_saloon: Type[repositories.beauty_saloon_repository.BeautySaloonRepository]
    saloon_spec: Type[repositories.saloon_spec_repository.SaloonSpecRepository]
    saloon_spec_service: Type[repositories.saloon_spec_service_repository.SaloonSpecServiceRepository]

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError
