<template>
  <div class="main-container">
    <div class="group">
      <div class="box">
        <div class="wrapper">
          <div class="group-2"><span class="text">9:41</span></div>
        </div>
        <div class="section">
          <div class="status-bar">
            <div class="true-depth-camera"></div>
            <div class="facetime-camera"></div>
          </div>
        </div>
        <div class="right-side">
          <div class="signal-wifi-battery">
            <div class="icon-mobile-signal"></div>
            <div class="wifi"></div>
            <div class="img-2"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="wrapper-2">
      <div class="img-3"></div>
      <span class="text-2" @click="goToChoseYourPuppy">Sign in with Google</span>
    </div>
    <div class="wrapper-3">
      <div class="img-4"></div>
      <span class="text-3" @click="goToChoseYourPuppy">Sign in with Apple</span>
    </div>
    <div class="section-3">
      <div class="pic-2"></div>
      <span class="text-4" @click="goToChoseYourPuppy">Sign in with email</span>
    </div>
    <div class="group-4">
      <div class="pic-3"></div>
      <span class="text-5" @click="goToChoseYourPuppy">Sign in with Account</span>
    </div>
    <div class="group-5">
      <div class="img-5"></div>
      <span class="text-6" @click="goToChoseYourPuppy">Sign in with Metamask</span>
    </div>
    <div class="box-5"></div>
    <div class="pic-4"></div>
    <span class="text-7">Run<br />Puppy</span>
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
.group {
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
.box {
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
.wrapper {
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
.group-2 {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.text {
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
.section {
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
.status-bar {
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
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.img-2 {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.wrapper-2 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 266px 0 0 32px;
  background: #1c1d1e;
  z-index: 19;
  border-radius: 10px;
}
.img-3 {
  position: absolute;
  width: 28px;
  height: 29px;
  top: 15px;
  left: 42px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/menu-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 32;
}
.text-2 {
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
.wrapper-3 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 21;
  border-radius: 10px;
}
.img-4 {
  position: absolute;
  width: 24.871px;
  height: 30.508px;
  top: 15px;
  left: 42px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/location-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 23;
}
.text-3 {
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
.section-3 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 24;
  border-radius: 10px;
}
.pic-2 {
  position: absolute;
  width: 33px;
  height: 33px;
  top: 14px;
  left: 39px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/profile-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 26;
  overflow: hidden;
}
.text-4 {
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
.group-4 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 27;
  border-radius: 10px;
}
.pic-3 {
  position: absolute;
  width: 35px;
  height: 35px;
  top: 12px;
  left: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/settings-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 29;
  overflow: hidden;
}
.text-5 {
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
.group-5 {
  position: relative;
  width: 330px;
  height: 60px;
  margin: 9px 0 0 32px;
  background: #1c1d1e;
  z-index: 30;
  border-radius: 10px;
}
.img-5 {
  position: absolute;
  width: 47px;
  height: 47px;
  top: 6px;
  left: 31px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/app-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 33;
  overflow: hidden;
}
.text-6 {
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
.box-5 {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 178px 0 0 130px;
  background: #000000;
  z-index: 15;
  border-radius: 100px;
}
.pic-4 {
  position: absolute;
  width: 63.898px;
  height: 71.201px;
  top: 167px;
  left: 116px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/103408/logo-image.svg)
    no-repeat center;
  background-size: cover;
  z-index: 17;
  overflow: hidden;
}
.text-7 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 114px;
  height: 68px;
  top: 170px;
  left: 189px;
  color: #000000;
  font-family: Tsukushi B Round Gothic, var(--default-font-family);
  font-size: 33.922977447509766px;
  font-weight: 400;
  line-height: 33.923px;
  text-align: left;
  text-overflow: initial;
  text-transform: uppercase;
  z-index: 18;
  overflow: hidden;
  -webkit-text-stroke: 1.413px #000000;
}


</style>
  