from db.db import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .schema import SnipCreate, SnipResponse, SnipUpdate
from ..rate_limit import limiter

router = APIRouter(tags=["snip"])

@router.get("/snips")
@limiter.limit("10/minute")
async def get_snips(session: Session = Depends(get_db)) -> list[SnipResponse]:
    with session as db:
        snips = db.query().all()
        if snips is None:
            raise HTTPException(status_code=404, detail="Snips not found")
        return [SnipResponse.from_orm(snip) for snip in snips]

@router.get("/snip/{id}")
@limiter.limit("10/minute")
async def get_snip(id: int, session: Session = Depends(get_db)) -> SnipResponse:
    with session as db:
        snip = db.query().filter_by(id=id).first()
        if snip is None:
            raise HTTPException(status_code=404, detail="Snip not found")
        return SnipResponse.from_orm(snip)

@router.post("/snip")
@limiter.limit("5/minute")
async def post_snip(snip: SnipCreate, session: Session = Depends(get_db)) -> SnipResponse:
    with session as db:
        db.add(snip)
        db.commit()
        db.refresh(snip)
        return SnipResponse.from_orm(snip)

@router.patch("/snip/{id}")
@limiter.limit("5/minute")
async def update_snip(id: int, data: SnipUpdate, session: Session = Depends(get_db)) -> SnipResponse:
    with session as db:
        snip = db.query().filter_by(id=id).first()
        if snip is None:
            raise HTTPException(status_code=404, detail="Snip not found")
        for key, value in data.dict(exclude_unset=True).items():
            setattr(snip, key, value)
        db.commit()
        db.refresh(snip)
        return SnipResponse.from_orm(snip)

@router.delete("/snip/{id}")
@limiter.limit("5/minute")
async def delete_snip(id: int, session: Session = Depends(get_db)) -> dict[str, str]:
    with session as db:
        snip = db.query().filter_by(id=id).first()
        if snip is None:
            raise HTTPException(status_code=404, detail="Snip not found")
        db.delete(snip)
        db.commit()
        return {"state": "Deleted"}
