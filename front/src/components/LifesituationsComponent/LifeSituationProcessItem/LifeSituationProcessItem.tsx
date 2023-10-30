import React, { FC, useState } from "react";
import Buttons from "../../Buttons/Buttons";
import icons from "../../../assets/icons/icons";
import { ILifeSituationProcess } from "../../../models/ILifeSituation";
import "./styles.scss";
import { useTypeSelector } from "../../../hooks/useTypedSelector";
import { useDispatch } from "react-redux";
import { DataPressActionCreators } from "../../../store/reducers/dataPressItem/action-creator";
import Modal from "../../Modal/Modal";
import FormInput from "../../FormInput/FormInput";
import { LifeSituationActionCreators } from "../../../store/reducers/lfieSituation/action-creatorlife";
import { fieldToArray } from "../../UI/functions/functions";
import ProcessesApiRequest from "../../../api/Processes/Processes";
import Checkbox from "../../Checkbox/Checkbox";
import { updateDataKey } from "../../UI/functions/updateDataKey/updateDataKey";

interface LifeSituationProcessItemProps {
  processes: ILifeSituationProcess | undefined;
  processesOption: any;
}

interface IProcesses {
  name: string | null;
  service: string | null;
  status: string | null;
  is_internal_client: boolean;
  is_external_client: boolean;
  responsible_authority: string | null;
  department: string | null;
  is_digital_format: boolean;
  is_non_digital_format: boolean;
  digital_format_link: string | null;
  identifier: string | null;
}

const LifeSituationProcessItem: FC<LifeSituationProcessItemProps> = ({
  processes,
  processesOption,
}) => {
  const lifeSituationProcessesApi = new ProcessesApiRequest();
  const [isVisibleModal, setIsVisibleModal] = useState<boolean>(false);
  const [isVisibleModalData, setIsVisibleModalData] = useState<boolean>(false);
  const { isUpdate } = useTypeSelector((state) => state.lifeSituationReducer);
  const dispatch = useDispatch();
  const { dataPress } = useTypeSelector((state) => state.dataPressReducer);
  const [identifier, setIdentifier] = useState<string>("");

  const handleChangeInput = (
    field: string,
    value: string,
    isChecked: boolean | undefined
  ) => {
    dispatch(
      DataPressActionCreators.setDataPress(field, isChecked ? isChecked : value)
    );
  };
  const handleChangeInputData = (
    field: string,
    value: string,
    isChecked: boolean | undefined
  ) => {
    const updatedMainInformation = {
      //@ts-ignore
      ...dataPress?.data,
      [field]: value,
    };

    dispatch(
      DataPressActionCreators.setDataPress("data", updatedMainInformation)
    );
  };

  const addLifeSituationServices = (type?: string) => {
    dispatch(DataPressActionCreators.setDataPress("identifier", identifier));
    type === "update"
      ? lifeSituationProcessesApi
          .update({
            urlParams: dataPress ? dataPress?.id + "/" : "",
            body: dataPress,
          })
          .then((resp) => {
            if (resp.success) {
              closeModal("update");
              dispatch(LifeSituationActionCreators.setUpdate(!isUpdate));
            }
          })
      : lifeSituationProcessesApi.create({ body: dataPress }).then((resp) => {
          if (resp.success) {
            closeModal("create");
            dispatch(LifeSituationActionCreators.setUpdate(!isUpdate));
          }
        });
  };

  const openModal = () => {
    lifeSituationProcessesApi.generateIdentifier().then((ident) => {
      if (ident.success) {
        //@ts-ignore
        setIdentifier(ident?.data?.identifier || "");
        setIsVisibleModal(true);
      }
    });
  };

  const processesOptionCreate = fieldToArray(processesOption.child.children);
  const processesOptionData = fieldToArray(
    processesOption.child.children.data.children
  );

  const openModalData = (process: IProcesses) => {
    console.log("====================================");
    console.log("process", process);
    console.log("====================================");
    fieldToArray(process).map(
      (item: { key: string; value: string | boolean }) => {
        dispatch(DataPressActionCreators.setDataPress(item.key, item.value));
      }
    );
    setIsVisibleModalData(true);
  };

  const closeModal = (type: string) => {
    type === "update" ? setIsVisibleModalData(false) : setIsVisibleModal(false);

    dispatch(DataPressActionCreators.clearDataPress());
  };

  console.log("====================================");
  console.log(processes);
  console.log("====================================");

  return (
    <>
      {isVisibleModal && (
        <Modal
          content={
            <div className="modalContainerGrid">
              <h1>Добавить процесс</h1>
              {processesOptionCreate != null &&
                processesOptionCreate.map((item: any) => {
                  if (item.key === "id" || item.key === "data") {
                    return null;
                  }

                  return (
                    <div key={item.key}>
                      <FormInput
                        key={item.key}
                        style={""}
                        value={
                          //@ts-ignore
                          item.key === "identifier"
                            ? identifier
                            : //@ts-ignore
                              dataPress[item.key]
                        }
                        options={item.value.choices}
                        disabled={item.key === "identifier" ? true : undefined}
                        onChange={(e, isChecked) => {
                          handleChangeInput(
                            item.key,
                            e,
                            isChecked && isChecked
                          );
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
                    closeModal("create");
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
            closeModal("create");
          }}
        />
      )}

      {isVisibleModalData && (
        <Modal
          content={
            <div className="modalContainerGrid">
              <h1>Данные процесса</h1>
              <FormInput
                key={""}
                style={""}
                value={
                  //@ts-ignore
                  dataPress?.name
                }
                disabled={true}
                onChange={() => {}}
                subInput={"Название процесса"}
                error={""}
                keyData={""}
                required={false}
                type={""}
              />
              {processesOptionData != null &&
                processesOptionData.map((item: any) => {
                  if (item.key === "id") {
                    return null;
                  }
                  console.log("====================================");
                  console.log("dddddd", dataPress);
                  console.log("====================================");
                  return (
                    <div key={item.key}>
                      <FormInput
                        key={item.key}
                        style={""}
                        value={
                          //@ts-ignore
                          item.key === "identifier"
                            ? identifier
                            : //@ts-ignore
                              dataPress?.data && dataPress?.data[item.key]
                        }
                        options={item.value.choices}
                        disabled={item.key === "identifier" ? true : undefined}
                        onChange={(e, isChecked) => {
                          handleChangeInputData(item.key, e, isChecked);
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
                    closeModal("update");
                  }}
                />
                <Buttons
                  className="buttonModal"
                  text={"Добавить"}
                  onClick={() => {
                    addLifeSituationServices("update");
                  }}
                />
              </div>
            </div>
          }
          onClose={() => {
            closeModal("update");
          }}
        />
      )}
      <div className="lifeSituationProcessContainer">
        {/*@ts-ignore*/}

        {processes?.map((proces) => (
          <div className="containerProcesses">
            <div key={proces?.id} className="cardLifeSituationServices">
              <div className="cardHeader">
                <h1 className="titleProcesses">{proces?.name}</h1>
                <div className="containerIdentProcesses">
                  <p className="processesIdent">{proces?.identifier}</p>
                  <p className="processesStatus">
                    {proces?.responsible_authority}
                  </p>
                  <Buttons
                    text={"Данные"}
                    ico={proces.data ? icons.checkBlack : ""}
                    className="buttonDataWhite"
                    onClick={() => {
                      openModalData(proces);
                    }}
                  />
                </div>
                <h1 className="processesDepartament">{proces.department}</h1>
                {proces?.digital_format_link && (
                  <a
                    className="linkProcesses"
                    href={proces?.digital_format_link}
                    target="_blank"
                  >
                    <img src={icons.linkExt}></img>
                    {proces?.digital_format_link}
                  </a>
                )}
              </div>
            </div>
          </div>
        ))}
        <Buttons
          ico={icons.plusCircle}
          text={"Добавить процесс"}
          className="whiteButtonAdd"
          onClick={() => {
            openModal();
          }}
        />
      </div>
    </>
  );
};

export default LifeSituationProcessItem;
