from fastapi import APIRouter

from .schema import SnipCreate, SnipResponse, SnipUpdate

router = APIRouter(tags=["snip"])

@router.get("/snips")
async def get_snips() -> list[SnipResponse]:
    """
        Ir na base de dados
        recolher dados
        entregar dados formatados
    """
    ...

@router.get("/snip/{id}")
async def get_snip(id: int) -> SnipResponse:
    """ A definir (back ou front).
        Ir na bd
        recolher o dado
        entregar dados formatados
    """
    ...

@router.post("/snip")
async def post_snip(snip: SnipCreate) -> SnipResponse:
    """
        Recebe dados
        valida e formata
        introduz na bd
    """
    ...

@router.patch("/snip/{id}")
async def update_snip(id: int, data: SnipUpdate):
    """
        Recebe dados para atualizar
        valida e formata
        reescreve na bd
    """
    ...

@router.delete("/snip/{id}")
async def delete_snip(id:int) -> dict[str,str]:
    """
        recebe id
        valida se ainda nao foi apagado e se existe
        deleta e retorna certificacao
    """
    return {"state":"Deleted"}
