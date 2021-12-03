from typing import Type, TypeVar

from django.db import models
from fastapi import HTTPException, Path

from policies.models import Contract

ModelT = TypeVar("ModelT", bound=models.Model)


async def retrieve_object(model_class: Type[ModelT], id: int) -> ModelT:
    """
    retrieve object by id 
    """
    instance = model_class.objects.get(pk=id)
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


async def retrieve_contract(contract_id: int) -> Contract:
    """
    retrieve contract by id
    """

    return await retrieve_object(Contract, contract_id)



async def retrieve_Contracts():
    """
    retrieve all contracts
    """
    return Contract.objects.all()
