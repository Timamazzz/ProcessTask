// types.ts
import { ILifeSituation } from "../../../models/ILifeSituation";

export interface LifeSituationState {
    lifeSituation: ILifeSituation[] | undefined;
    isLoading: boolean;
    isUpdate: boolean;
    error: string;
}

export enum LifeSituationActionEnum {
    SET_LIFESITUATION = 'SET_LIFESITUATION',
    SET_ERROR = 'SET_ERROR',
    SET_UPDATE = 'SET_UPDATE',
}

export interface SetLifeSituationAction {
    type: LifeSituationActionEnum.SET_LIFESITUATION;
    payload: ILifeSituation[];
}

export interface SetErrorAction {
    type: LifeSituationActionEnum.SET_ERROR;
    payload: string;
}
export interface SetUpdateAction {
    type: LifeSituationActionEnum.SET_UPDATE;
    payload: boolean;
}

export type LifeSituationAction = 
    SetLifeSituationAction |
    SetErrorAction|
    SetUpdateAction