import React, { FC, useState } from "react";
import FormInput from "../../FormInput/FormInput";
import { useDispatch } from "react-redux";
import { useTypeSelector } from "../../../hooks/useTypedSelector";
import Buttons from "../../Buttons/Buttons";
import icons from "../../../assets/icons/icons";

interface LoginForgotProps {
  onAuth: () => void;
}

const LoginFormForgot: FC<LoginForgotProps> = ({ onAuth }) => {
  const dispatch = useDispatch();

  const { error, isLoading } = useTypeSelector((state) => state.authReducer);

  const [emeil, setEmail] = useState("");

  const submit = () => {
    //@ts-ignore
    dispatch(AuthActionCreators.login(username, password));
  };
  return (
    <>
      <h1>Восстановление пароля</h1>
      <FormInput
        style={""}
        value={undefined}
        onChange={(e) => {
          setEmail(e);
        }}
        subInput={"Электронная почта"}
        required={true}
        error={error}
        keyData={""}
        loading={isLoading}
        type="email"
        friedlyInput={true}
      />
      <Buttons
        ico={isLoading ? icons.lock : ""}
        text={"Отправить"}
        onClick={() => {
          submit();
        }}
        className="buttonLogin"
      />
      <p
        className="backButton"
        onClick={() => {
          onAuth();
        }}
      >
        Вернуться назад
      </p>
    </>
  );
};

export default LoginFormForgot;
