
from typing import List

from fastapi import APIRouter, Depends

from policies.api import views
from policies.models import Contract
from policies.schemas import Contract, Contracts

router = APIRouter()


@router.get("/")
def get_contracts(
    contracts: List[Contract] = Depends(views.retrieve_Contracts),
) -> Contracts:
    return Contracts.from_qs(contracts)


@router.get("/{c_id}")
def get_contract(contract: Contract = Depends(views.retrieve_contract)) -> Contract:
    return Contract.from_orm(contract)
