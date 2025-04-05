<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="time-edit">9:41</span></div>
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
      <div class="pinterest-download"></div>
      <span class="running-companion">那个陪伴你跑步的它...</span>
      <div class="frame" @click="goToLogin"><span class="login">login</span></div>
      <div class="home-indicator"></div>
      <div class="logo"></div>
      <span class="pet">pet</span>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goToLogin = () => {
  router.push({ name: 'Login' });
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
  .time-edit {
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
    background: url(https://static.codia.ai/custom_image/2025-04-05/175222/mobile-signal-icon.svg)
      no-repeat center;
    background-size: cover;
    z-index: 11;
  }
  .wifi {
    flex-shrink: 0;
    position: relative;
    width: 17px;
    height: 11.834px;
    background: url(https://static.codia.ai/custom_image/2025-04-05/175222/wifi-icon.svg)
      no-repeat center;
    background-size: 100% 100%;
    z-index: 12;
  }
  .status-bar-battery {
    flex-shrink: 0;
    position: relative;
    width: 27.401px;
    height: 13px;
    background: url(https://static.codia.ai/custom_image/2025-04-05/175222/battery-icon.svg)
      no-repeat center;
    background-size: cover;
    z-index: 13;
  }
  .pinterest-download {
    position: relative;
    width: 316px;
    height: 221px;
    margin: 211px 0 0 39px;
    background: url(https://static.codia.ai/custom_image/2025-04-05/175222/pinterest-download-image.png)
      no-repeat center;
    background-size: cover;
    z-index: 19;
  }
  .running-companion {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    position: relative;
    width: 218px;
    height: 24px;
    margin: 37px 0 0 88px;
    color: #000000;
    font-family: Inter, var(--default-font-family);
    font-size: 22.18531608581543px;
    font-weight: 400;
    line-height: 24px;
    text-align: center;
    text-transform: uppercase;
    white-space: nowrap;
    z-index: 20;
  }
  .frame {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: nowrap;
    gap: 65px;
    position: relative;
    width: 334px;
    height: 59px;
    margin: 176px 0 0 30px;
    padding: 5px 6px 5px 6px;
    background: #ff5218;
    z-index: 21;
    border-radius: 29.5px;
  }
  .login {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    flex-shrink: 0;
    flex-basis: auto;
    position: relative;
    width: 48px;
    height: 25px;
    color: #ffffff;
    font-family: Inter, var(--default-font-family);
    font-size: 20.448429107666016px;
    font-weight: 500;
    line-height: 24.747px;
    text-align: center;
    white-space: nowrap;
    z-index: 22;
  }
  .home-indicator {
    position: relative;
    width: 134px;
    height: 5px;
    margin: 52px 0 0 130px;
    background: #000000;
    z-index: 15;
    border-radius: 100px;
  }
  .logo {
    position: absolute;
    width: 35px;
    height: 39px;
    top: 116px;
    left: 33px;
    background: url(https://static.codia.ai/custom_image/2025-04-05/175222/pet-logo.svg)
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
    width: 46px;
    height: 32px;
    top: 119px;
    left: 76px;
    color: #000000;
    font-family: Tsukushi B Round Gothic, var(--default-font-family);
    font-size: 31.725000381469727px;
    font-weight: 400;
    line-height: 31.725px;
    text-align: center;
    text-transform: capitalize;
    white-space: nowrap;
    z-index: 18;
    -webkit-text-stroke: 1.322px #000000;
  }
  
</style>
  