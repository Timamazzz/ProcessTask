import React, { FC, useEffect, useState } from "react";
import { ILifeSituationServices } from "../../../models/ILifeSituation";
import Buttons from "../../Buttons/Buttons";
import icons from "../../../assets/icons/icons";
import "../styles.scss";
import LifeSituationProcessItem from "../LifeSituationProcessItem/LifeSituationProcessItem";
import Modal from "../../Modal/Modal";
import { DataPressActionCreators } from "../../../store/reducers/dataPressItem/action-creator";
import { fieldToArray } from "../../UI/functions/functions";
import FormInput from "../../FormInput/FormInput";
import { useTypeSelector } from "../../../hooks/useTypedSelector";
import LifesituationsApiRequest from "../../../api/Lifesituation/Lifesituation";
import { useDispatch } from "react-redux";
import ServicesApiRequest from "../../../api/Services/Services";
import { LifeSituationActionCreators } from "../../../store/reducers/lfieSituation/action-creatorlife";

interface LifeSituationServiceItemProps {
  services: ILifeSituationServices | undefined;
  servicesOption: any;
  lifeSitaitonsId: string | undefined;
  lifeSituationActive?: any;
}

const LifeSituationServiceItem: FC<LifeSituationServiceItemProps> = ({
  services,
  servicesOption,
  lifeSitaitonsId,
  lifeSituationActive,
}) => {
  const lifeSituationServicesApi = new ServicesApiRequest();
  const [isVisibleModal, setIsVisibleModal] = useState<boolean>(false);
  const { isUpdate } = useTypeSelector((state) => state.lifeSituationReducer);

  const { dataPress } = useTypeSelector((state) => state.dataPressReducer);
  const dispatch = useDispatch();

  const handleChangeInput = (field: string, value: string | boolean) => {
    dispatch(DataPressActionCreators.setDataPress(field, value));
  };

  const addLifeSituationServices = (type?: string) => {
    lifeSituationServicesApi.create({ body: dataPress }).then((resp) => {
      if (resp.success) {
        setIsVisibleModal(false);
        dispatch(LifeSituationActionCreators.setUpdate(!isUpdate));
      }
    });
  };

  const [selectedCards, setSelectedCards] = useState<string[]>([]);

  const toggleCardSelection = (id: string) => {
    if (selectedCards.includes(id)) {
      setSelectedCards(selectedCards.filter((cardId) => cardId !== id));
    } else {
      setSelectedCards([...selectedCards, id]);
    }
    dispatch(DataPressActionCreators.setDataPress("service", id ? id : ""));
  };

  const closeModal = (type?: string) => {
    setIsVisibleModal(false);

    dispatch(DataPressActionCreators.clearDataPress());
  };

  const servOptionData = fieldToArray(servicesOption.services.child.children);
  return (
    <>
      {isVisibleModal && (
        <Modal
          content={
            <div className="modalContainerGrid">
              <h1>Добавить услугу/функцию/сервис</h1>
              {servOptionData != null &&
                servOptionData.map((item: any) => {
                  if (item.key === "id" || item.key === "processes") {
                    return null;
                  }

                  return (
                    <div key={item.key}>
                      <FormInput
                        key={item.key}
                        style={""}
                        value={
                          //@ts-ignore
                          dataPress && dataPress[item.key]
                        }
                        options={item.value.choices}
                        disabled={item.key === "identifier" ? true : undefined}
                        onChange={(e) => {
                          handleChangeInput(item.key, e);
                        }}
                        subInput={item.value.label}
                        error={""}
                        keyData={item.key}
                        required={item.value.required}
                        type={item.value.type}
                      />
                    </div>
                  );
                })}
              <div className="modalButtonContainer">
                <Buttons
                  className="buttonModal_white"
                  text={"Отмена"}
                  onClick={() => {
                    closeModal();
                  }}
                />
                <Buttons
                  className="buttonModal"
                  text={"Добавить"}
                  onClick={() => {
                    addLifeSituationServices();
                  }}
                />
              </div>
            </div>
          }
          onClose={() => {
            closeModal();
          }}
        />
      )}
      <div
        className={`lifeSituationServiceContainer ${
          lifeSituationActive && "flexGrid"
        }`}
      >
        {/*@ts-ignore*/}
        {services?.map((service) => (
          <div className="containerServiceProcesses">
            <div
              key={service.id}
              className="cardLifeSituationServices"
              onClick={() => service?.id && toggleCardSelection(service.id)}
            >
              <div className="cardHeader">
                <h3 className="cardHeaderSubtitle">Услуга</h3>
                <h1>{service.name}</h1>
              </div>
              <div className="cardFooter">
                <p className="cardFooterNumber">
                  {service.regulating_act || ""}
                </p>
              </div>
            </div>
            {selectedCards.includes(service.id ? service.id : "") && (
              <LifeSituationProcessItem
                processes={service.processes}
                processesOption={
                  servicesOption.services.child.children.processes
                }
              />
            )}
          </div>
        ))}
        {!lifeSituationActive && (
          <Buttons
            ico={icons.plusCircle}
            text={"Добавить услугу/функцию/сервис"}
            className="whiteButtonAdd"
            onClick={() => {
              setIsVisibleModal(true);
            }}
          />
        )}
      </div>
    </>
  );
};

export default LifeSituationServiceItem;
