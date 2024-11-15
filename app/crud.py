from fastapi import Depends, HTTPException, APIRouter, status
from database import get_db
from models import SpyCats, Mission, Target
from schemas import CreateSpyCat, CreateMission
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/cats/", response_model=CreateSpyCat)
def create_cat(cat: CreateSpyCat, db: Session = Depends(get_db)):
    db_cat = SpyCats(**cat.model_dump())
    db.add(db_cat)
    db.commit()
    db.refresh()
    return db_cat


@router.get("/cats/")
def list_cats(db: Session = Depends(get_db)):
    return db.query(SpyCats).all()


@router.get("/cats/{cat_id}", response_model=CreateSpyCat)
def get_cat(cat_id: int, db: Session = Depends(get_db)):
    cat = db.query(SpyCats).filter(SpyCats.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat


@router.delete("/cats/{cat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    cat = db.query(SpyCats).filter(SpyCats.id == cat_id).first()
    if cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")

    if cat.mission:
        raise HTTPException(status_code=400, detail="Cat is assigned to a mission and cannot be deleted")

    db.delete(cat)
    db.commit()
    return {"detail": "Cat deleted successfully"}


@router.post("/missions/", response_model=CreateMission)
def create_mission(mission: CreateMission, db: Session = Depends(get_db)):
    if len(mission.targets) < 1 or len(mission.targets) > 3:
        raise HTTPException(status_code=400, detail="Target must be between 1 and 3")

    active_mission = db.query(Mission).filter_by(cat_id=mission.cat_id, is_complete=False).first()
    if active_mission:
        raise HTTPException(status_code=400, detail="This cat already has an active mission.")

    db_mission = Mission(cat_id=mission.cat_id, complete=mission.complete)
    db.add(db_mission)
    db.commit()
    db.refresh()

    for target_data in mission.targets:
        db_target = Target(**target_data, mission_id=db_mission.id)
        db.add(db_target)

    db.commit()
    db.refresh(db_mission)
    return db_mission


@router.get("/missions/")
def list_missions(db: Session = Depends(get_db)):
    return db.query(Mission).all()


@router.get("/missions/{mission_id}", response_model=CreateMission)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission


@router.put("/missions/{mission_id}/complete")
def complete_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    if mission.complete:
        raise HTTPException(status_code=400, detail="Mission is completed already")

    mission.complete = True
    for target in mission.targets:
        if target.complete:
            target.notes = "Notes are frozen, updates are forbidden"

    db.commit()
    return {"message": "Mission completed"}


@router.delete("/missions/{mission_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")

    if mission.cat_id is not None:
        raise HTTPException(status_code=400, detail="Mission is assigned to a cat and cannot be deleted")

    db.delete(mission)
    db.commit()
    return {"detail": "Mission deleted successfully"}


@router.put("/target/{target_id}/complete")
def complete_target(target_id: int, db: Session = Depends(get_db)):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    if target.complete:
        raise HTTPException(status_code=400, detail="Target is completed already")

    target.complete = True

    db.commit()
    return {"message": "Target completed"}


@router.put("/target/{target_id}/notes")
def update_target_notes(target_id: int, notes: str, db: Session = Depends(get_db)):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    if target.complete:
        raise HTTPException(status_code=400, detail="Target is completed already")

    target.notes = notes

    db.commit()
    return {"message": "Notes added"}
