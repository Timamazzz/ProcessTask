import React, { FC, useEffect, useState } from "react";
import Tabs from "../Tabs/Tabs";
import InputSearch from "../InputSearch/InputSearch";
import "./styles.scss";
import Buttons from "../Buttons/Buttons";
import LifesituationsComponent from "../LifesituationsComponent/LifesituationsComponent";
import LifesituationsApiRequest from "../../api/Lifesituation/Lifesituation";
import { useDispatch } from "react-redux";
import { LifeSituationActionCreators } from "../../store/reducers/lfieSituation/action-creatorlife";
import { ILifeSituation } from "../../models/ILifeSituation";
import { useTypeSelector } from "../../hooks/useTypedSelector";
import Modal from "../Modal/Modal";
import FormInput from "../FormInput/FormInput";
import { fieldToArray } from "../UI/functions/functions";
import { DataPressActionCreators } from "../../store/reducers/dataPressItem/action-creator";
import { IDataPress } from "../../models/IDataPress";
import LifeSituationServiceItem from "../LifesituationsComponent/LifeSituationServiceItem/LifeSituationServiceItem";

const ReestrComponent: FC = () => {
  const lifeSituationApi = new LifesituationsApiRequest();
  const { lifeSituation, isUpdate } = useTypeSelector(
    (state) => state.lifeSituationReducer
  );
  const { dataPress } = useTypeSelector((state) => state.dataPressReducer);
  const dispatch = useDispatch();
  const [activeTabId, setActiveTabId] = useState<number>(1);
  const [isVisibleModal, setIsVisibleModal] = useState<boolean>(false);
  const [identifier, setIdentifier] = useState<string>("");
  const [lifeSituationOption, setLifeSituationOption] = useState<any>(null);
  // const [isUpdate, setIsUpdate] = useState<boolean>(false);

  const tabsData = [
    {
      id: 1,
      text: "Жизненные ситуации",
      content: "",
    },
    {
      id: 2,
      text: "Услуги",
      content: "",
    },
  ];

  useEffect(() => {
    lifeSituationApi.list().then((resp) => {
      if (resp.success) {
        optionLifeSituation();
        dispatch(
          LifeSituationActionCreators.setLifeSituation(
            resp.data as ILifeSituation[]
          )
        );
      }
    });
  }, [isUpdate]);

  const optionLifeSituation = () => {
    lifeSituationApi.options().then((resp) => {
      if (resp.success) {
        //@ts-ignore
        const options = fieldToArray(resp?.data?.actions);
        setLifeSituationOption(options);
        lifeSituationApi.generateIdentifier().then((ident) => {
          if (ident.success) {
            //@ts-ignore
            setIdentifier(ident?.data?.identifier || "");
          }
        });
      }
    });
  };

  const handleChangeInput = (field: string, value: string | boolean) => {
    dispatch(DataPressActionCreators.setDataPress(field, value));
  };

  const addLifeSituation = (type?: string) => {
    dispatch(DataPressActionCreators.setDataPress("identifier", identifier));
    lifeSituationApi.create({ body: dataPress }).then((resp) => {
      if (resp.success) {
        setIsVisibleModal(false);
        dispatch(LifeSituationActionCreators.setUpdate(!isUpdate));
      }
    });
  };

  return (
    <>
      {isVisibleModal && (
        <Modal
          content={
            <div>
              <h1>Добавить жизненную ситуацию</h1>
              {lifeSituationOption != null &&
                lifeSituationOption.map((item: any) => {
                  if (item.key === "create") {
                    const optionData = fieldToArray(item.value);
                    return (
                      <div key={item.key}>
                        {optionData.map((data) => (
                          <FormInput
                            key={data.key}
                            style={""}
                            value={
                              data.key === "identifier" ? identifier : undefined
                            }
                            disabled={
                              data.key === "identifier" ? true : undefined
                            }
                            onChange={(e) => {
                              handleChangeInput(data.key, e);
                            }}
                            subInput={data.value.label}
                            error={""}
                            keyData={data.key}
                            required={data.value.required}
                            type={data.value.type}
                          />
                        ))}
                      </div>
                    );
                  } else {
                    return null; // Можете добавить обработку других случаев, если необходимо
                  }
                })}
              <div className="modalButtonContainer">
                <Buttons
                  className="buttonModal_white"
                  text={"Отмена"}
                  onClick={() => {
                    setIsVisibleModal(false);
                  }}
                />
                <Buttons
                  className="buttonModal"
                  text={"Добавить"}
                  onClick={() => {
                    addLifeSituation();
                  }}
                />
              </div>
            </div>
          }
          onClose={() => {
            setIsVisibleModal(false);
          }}
        />
      )}

      <div className="reestrComponent">
        <div className="reestrNav">
          <Tabs tabsData={tabsData} activeTabId={setActiveTabId} />
          <InputSearch items={[]} />
          <Buttons
            text={"Добавить жизненную ситуацию"}
            className="whiteButton"
            onClick={() => {
              setIsVisibleModal(true);
            }}
          />
        </div>

        {activeTabId === 1 ? (
          <LifesituationsComponent
            lifeSituation={lifeSituation}
            lifeSituationOption={lifeSituationOption}
          />
        ) : (
          lifeSituation?.map((item) => {
            return (
              <LifeSituationServiceItem
                lifeSitaitonsId={item.id}
                services={item.services}
                lifeSituationActive={true}
                servicesOption={
                  lifeSituationOption?.find(
                    (option: { key: string }) => option.key === "list"
                  )?.value
                }
              />
            );
          })
        )}
      </div>
    </>
  );
};

export default ReestrComponent;
