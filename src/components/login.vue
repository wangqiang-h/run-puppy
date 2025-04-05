<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="time">9:41</span></div>
          </div>
          <div class="dynamic-island">
            <div class="status-bar-1">
              <div class="true-depth-camera"></div>
              <div class="facetime-camera"></div>
            </div>
          </div>
          <div class="right-side">
            <div class="signal-wifi-battery">
              <div class="icon-mobile-signal"></div>
              <div class="wifi"></div>
              <div class="status-bar-battery"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame">
        <div class="image"></div>
        <span class="sign-in-google" @click="goToChoseYourPuppy">Sign in with Google</span>
      </div>
      <div class="frame-2">
        <div class="mask-group"></div>
        <span class="sign-in-apple" @click="goToChoseYourPuppy">Sign in with Apple</span>
      </div>
      <div class="frame-3">
        <div class="email-sign-in"></div>
        <span class="sign-in-email" @click="goToChoseYourPuppy">Sign in with email</span>
      </div>
      <div class="frame-4">
        <div class="account"></div>
        <span class="account-sign-in" @click="goToChoseYourPuppy">Sign in with Account</span>
      </div>
      <div class="frame-5">
        <div class="account-balance"></div>
        <span class="sign-in-metamask" @click="goToChoseYourPuppy">Sign in with Metamask</span>
      </div>
      <div class="home-indicator"></div>
      <div class="logo"></div>
      <span class="pet">pet</span>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goToChoseYourPuppy = () => {
  router.push({ name: 'choose_your_puppy' });
};
</script>
  
  <style scoped>
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
    "Source Han Sans CN", sans-serif;
}

.main-container {
  overflow: hidden;
}

.main-container,
.main-container * {
  box-sizing: border-box;
}

input,
select,
textarea,
button {
  outline: 0;
}

.main-container {
  position: relative;
  width: 393px;
  height: 852px;
  margin: 0 auto;
  background: #ffffff;
  overflow: hidden;
}
.top-navigation {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  background: #ffffff;
  backdrop-filter: blur(10px);
}
.status-bar {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 1;
}
.left-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 0 3px 10px;
  z-index: 2;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.time {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 54px;
  height: 20px;
  top: 1px;
  left: 0;
  color: #000000;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.dynamic-island {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 125px;
  min-height: 0;
  z-index: 5;
}
.status-bar-1 {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.true-depth-camera {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 7;
  overflow: hidden;
  border-radius: 100px;
}
.facetime-camera {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 8;
  overflow: hidden;
  border-radius: 100px;
}
.right-side {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 11px 0 0;
  z-index: 9;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.frame {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 266px 0 0 32px;
  background: #1c1d1e;
  z-index: 19;
  border-radius: 10px;
}
.image {
  position: absolute;
  width: 28px;
  height: 29px;
  top: 15px;
  left: 42px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/google-logo.png)
    no-repeat center;
  background-size: cover;
  z-index: 32;
}
.sign-in-google {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22px;
  top: 19px;
  left: 98px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 400;
  line-height: 21.8px;
  text-align: left;
  white-space: nowrap;
  letter-spacing: -0.4px;
  z-index: 20;
}
.frame-2 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 21;
  border-radius: 10px;
}
.mask-group {
  position: absolute;
  width: 24.871px;
  height: 30.508px;
  top: 15px;
  left: 42px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/apple-logo.png)
    no-repeat center;
  background-size: cover;
  z-index: 23;
}
.sign-in-apple {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22px;
  top: 19px;
  left: calc(50% - 67px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 400;
  line-height: 21.8px;
  text-align: left;
  white-space: nowrap;
  letter-spacing: -0.4px;
  z-index: 22;
}
.frame-3 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 24;
  border-radius: 10px;
}
.email-sign-in {
  position: absolute;
  width: 33px;
  height: 33px;
  top: 14px;
  left: 39px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/email-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 26;
  overflow: hidden;
}
.sign-in-email {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22px;
  top: 19px;
  left: calc(50% - 67px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 400;
  line-height: 21.8px;
  text-align: left;
  white-space: nowrap;
  letter-spacing: -0.4px;
  z-index: 25;
}
.frame-4 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 27;
  border-radius: 10px;
}
.account {
  position: absolute;
  width: 35px;
  height: 35px;
  top: 12px;
  left: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/account-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 29;
  overflow: hidden;
}
.account-sign-in {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22px;
  top: 19px;
  left: calc(50% - 67px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 400;
  line-height: 21.8px;
  text-align: left;
  white-space: nowrap;
  letter-spacing: -0.4px;
  z-index: 28;
}
.frame-5 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 30;
  border-radius: 10px;
}
.account-balance {
  position: absolute;
  width: 47px;
  height: 47px;
  top: 6px;
  left: 31px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/metamask-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 33;
  overflow: hidden;
}
.sign-in-metamask {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22px;
  top: 19px;
  left: 98px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 400;
  line-height: 21.8px;
  text-align: left;
  white-space: nowrap;
  letter-spacing: -0.4px;
  z-index: 31;
}
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 178px 0 0 130px;
  background: #000000;
  z-index: 15;
  border-radius: 100px;
}
.logo {
  position: absolute;
  width: 63.898px;
  height: 71.201px;
  top: 167px;
  left: 116px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/175732/app-logo.svg)
    no-repeat center;
  background-size: cover;
  z-index: 17;
  overflow: hidden;
}
.pet {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 83.981px;
  height: 58.421px;
  top: 172.477px;
  left: 194.504px;
  color: #000000;
  font-family: Tsukushi B Round Gothic, var(--default-font-family);
  font-size: 57.91941833496094px;
  font-weight: 400;
  line-height: 57.919px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 18;
  -webkit-text-stroke: 2.413px #000000;
}

</style>
  