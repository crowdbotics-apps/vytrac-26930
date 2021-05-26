import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen102201245Navigator from '../features/BlankScreen102201245/navigator';
import BlankScreen101201183Navigator from '../features/BlankScreen101201183/navigator';
import BlankScreen100201182Navigator from '../features/BlankScreen100201182/navigator';
import BlankScreen99201181Navigator from '../features/BlankScreen99201181/navigator';
import BlankScreen98201180Navigator from '../features/BlankScreen98201180/navigator';
import BlankScreen97201179Navigator from '../features/BlankScreen97201179/navigator';
import CopyOfBlankScreen80200733Navigator from '../features/CopyOfBlankScreen80200733/navigator';
import BlankScreen96200732Navigator from '../features/BlankScreen96200732/navigator';
import BlankScreen95200731Navigator from '../features/BlankScreen95200731/navigator';
import BlankScreen94200730Navigator from '../features/BlankScreen94200730/navigator';
import BlankScreen93200729Navigator from '../features/BlankScreen93200729/navigator';
import BlankScreen92200728Navigator from '../features/BlankScreen92200728/navigator';
import BlankScreen91200727Navigator from '../features/BlankScreen91200727/navigator';
import BlankScreen90200726Navigator from '../features/BlankScreen90200726/navigator';
import BlankScreen89200725Navigator from '../features/BlankScreen89200725/navigator';
import BlankScreen88200724Navigator from '../features/BlankScreen88200724/navigator';
import BlankScreen87200723Navigator from '../features/BlankScreen87200723/navigator';
import BlankScreen86200722Navigator from '../features/BlankScreen86200722/navigator';
import BlankScreen85200707Navigator from '../features/BlankScreen85200707/navigator';
import BlankScreen84200706Navigator from '../features/BlankScreen84200706/navigator';
import BlankScreen83200703Navigator from '../features/BlankScreen83200703/navigator';
import BlankScreen82200702Navigator from '../features/BlankScreen82200702/navigator';
import BlankScreen81200701Navigator from '../features/BlankScreen81200701/navigator';
import BlankScreen80200700Navigator from '../features/BlankScreen80200700/navigator';
import BlankScreen79200699Navigator from '../features/BlankScreen79200699/navigator';
import BlankScreen78200698Navigator from '../features/BlankScreen78200698/navigator';
import BlankScreen77200697Navigator from '../features/BlankScreen77200697/navigator';
import BlankScreen76200696Navigator from '../features/BlankScreen76200696/navigator';
import BlankScreen74200694Navigator from '../features/BlankScreen74200694/navigator';
import CopyOfCopyOfBlankScreen34200693Navigator from '../features/CopyOfCopyOfBlankScreen34200693/navigator';
import CopyOfCopyOfBlankScreen34200692Navigator from '../features/CopyOfCopyOfBlankScreen34200692/navigator';
import CopyOfCopyOfBlankScreen34200691Navigator from '../features/CopyOfCopyOfBlankScreen34200691/navigator';
import CopyOfCopyOfBlankScreen34200690Navigator from '../features/CopyOfCopyOfBlankScreen34200690/navigator';
import BlankScreen69200688Navigator from '../features/BlankScreen69200688/navigator';
import BlankScreen68200687Navigator from '../features/BlankScreen68200687/navigator';
import BlankScreen67200686Navigator from '../features/BlankScreen67200686/navigator';
import BlankScreen66200685Navigator from '../features/BlankScreen66200685/navigator';
import BlankScreen65200684Navigator from '../features/BlankScreen65200684/navigator';
import BlankScreen64200683Navigator from '../features/BlankScreen64200683/navigator';
import CopyOfBlankScreen34200682Navigator from '../features/CopyOfBlankScreen34200682/navigator';
import CopyOfBlankScreen34200681Navigator from '../features/CopyOfBlankScreen34200681/navigator';
import CopyOfBlankScreen34200680Navigator from '../features/CopyOfBlankScreen34200680/navigator';
import CopyOfBlankScreen34200679Navigator from '../features/CopyOfBlankScreen34200679/navigator';
import CopyOfBlankScreen34200678Navigator from '../features/CopyOfBlankScreen34200678/navigator';
import CopyOfBlankScreen34200677Navigator from '../features/CopyOfBlankScreen34200677/navigator';
import CopyOfBlankScreen34200676Navigator from '../features/CopyOfBlankScreen34200676/navigator';
import CopyOfBlankScreen34200675Navigator from '../features/CopyOfBlankScreen34200675/navigator';
import CopyOfBlankScreen34200674Navigator from '../features/CopyOfBlankScreen34200674/navigator';
import CopyOfBlankScreen34200673Navigator from '../features/CopyOfBlankScreen34200673/navigator';
import CopyOfBlankScreen34200672Navigator from '../features/CopyOfBlankScreen34200672/navigator';
import CopyOfBlankScreen34200671Navigator from '../features/CopyOfBlankScreen34200671/navigator';
import CopyOfBlankScreen34200670Navigator from '../features/CopyOfBlankScreen34200670/navigator';
import CopyOfBlankScreen34200669Navigator from '../features/CopyOfBlankScreen34200669/navigator';
import CopyOfBlankScreen34200668Navigator from '../features/CopyOfBlankScreen34200668/navigator';
import CopyOfBlankScreen34200667Navigator from '../features/CopyOfBlankScreen34200667/navigator';
import CopyOfBlankScreen34200666Navigator from '../features/CopyOfBlankScreen34200666/navigator';
import CopyOfBlankScreen34200665Navigator from '../features/CopyOfBlankScreen34200665/navigator';
import CopyOfBlankScreen34200664Navigator from '../features/CopyOfBlankScreen34200664/navigator';
import CopyOfBlankScreen34200663Navigator from '../features/CopyOfBlankScreen34200663/navigator';
import CopyOfBlankScreen34200662Navigator from '../features/CopyOfBlankScreen34200662/navigator';
import CopyOfBlankScreen34200661Navigator from '../features/CopyOfBlankScreen34200661/navigator';
import CopyOfBlankScreen34200660Navigator from '../features/CopyOfBlankScreen34200660/navigator';
import CopyOfBlankScreen34200659Navigator from '../features/CopyOfBlankScreen34200659/navigator';
import CopyOfBlankScreen34200658Navigator from '../features/CopyOfBlankScreen34200658/navigator';
import CopyOfBlankScreen34200657Navigator from '../features/CopyOfBlankScreen34200657/navigator';
import CopyOfBlankScreen34200656Navigator from '../features/CopyOfBlankScreen34200656/navigator';
import CopyOfBlankScreen34200655Navigator from '../features/CopyOfBlankScreen34200655/navigator';
import CopyOfBlankScreen34200654Navigator from '../features/CopyOfBlankScreen34200654/navigator';
import CopyOfBlankScreen34200653Navigator from '../features/CopyOfBlankScreen34200653/navigator';
import CopyOfBlankScreen34200652Navigator from '../features/CopyOfBlankScreen34200652/navigator';
import BlankScreen34200651Navigator from '../features/BlankScreen34200651/navigator';
import BlankScreen33200636Navigator from '../features/BlankScreen33200636/navigator';
import BlankScreen32200635Navigator from '../features/BlankScreen32200635/navigator';
import BlankScreen31200634Navigator from '../features/BlankScreen31200634/navigator';
import BlankScreen30200633Navigator from '../features/BlankScreen30200633/navigator';
import BlankScreen29200632Navigator from '../features/BlankScreen29200632/navigator';
import BlankScreen28200614Navigator from '../features/BlankScreen28200614/navigator';
import BlankScreen27200542Navigator from '../features/BlankScreen27200542/navigator';
import BlankScreen24200539Navigator from '../features/BlankScreen24200539/navigator';
import BlankScreen23200489Navigator from '../features/BlankScreen23200489/navigator';
import BlankScreen22200488Navigator from '../features/BlankScreen22200488/navigator';
import BlankScreen20200351Navigator from '../features/BlankScreen20200351/navigator';
import BlankScreen19200350Navigator from '../features/BlankScreen19200350/navigator';
import BlankScreen18200326Navigator from '../features/BlankScreen18200326/navigator';
import BlankScreen17200323Navigator from '../features/BlankScreen17200323/navigator';
import BlankScreen16200317Navigator from '../features/BlankScreen16200317/navigator';
import BlankScreen15200312Navigator from '../features/BlankScreen15200312/navigator';
import BlankScreen13200310Navigator from '../features/BlankScreen13200310/navigator';
import BlankScreen12200309Navigator from '../features/BlankScreen12200309/navigator';
import BlankScreen11200308Navigator from '../features/BlankScreen11200308/navigator';
import BlankScreen10200307Navigator from '../features/BlankScreen10200307/navigator';
import BlankScreen9200306Navigator from '../features/BlankScreen9200306/navigator';
import BlankScreen8200305Navigator from '../features/BlankScreen8200305/navigator';
import BlankScreen7200304Navigator from '../features/BlankScreen7200304/navigator';
import BlankScreen6200303Navigator from '../features/BlankScreen6200303/navigator';
import BlankScreen5200302Navigator from '../features/BlankScreen5200302/navigator';
import BlankScreen4200301Navigator from '../features/BlankScreen4200301/navigator';
import BlankScreen3200300Navigator from '../features/BlankScreen3200300/navigator';
import BlankScreen2200299Navigator from '../features/BlankScreen2200299/navigator';
import BlankScreen1200298Navigator from '../features/BlankScreen1200298/navigator';
import BlankScreen0200297Navigator from '../features/BlankScreen0200297/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen102201245: { screen: BlankScreen102201245Navigator },
BlankScreen101201183: { screen: BlankScreen101201183Navigator },
BlankScreen100201182: { screen: BlankScreen100201182Navigator },
BlankScreen99201181: { screen: BlankScreen99201181Navigator },
BlankScreen98201180: { screen: BlankScreen98201180Navigator },
BlankScreen97201179: { screen: BlankScreen97201179Navigator },
CopyOfBlankScreen80200733: { screen: CopyOfBlankScreen80200733Navigator },
BlankScreen96200732: { screen: BlankScreen96200732Navigator },
BlankScreen95200731: { screen: BlankScreen95200731Navigator },
BlankScreen94200730: { screen: BlankScreen94200730Navigator },
BlankScreen93200729: { screen: BlankScreen93200729Navigator },
BlankScreen92200728: { screen: BlankScreen92200728Navigator },
BlankScreen91200727: { screen: BlankScreen91200727Navigator },
BlankScreen90200726: { screen: BlankScreen90200726Navigator },
BlankScreen89200725: { screen: BlankScreen89200725Navigator },
BlankScreen88200724: { screen: BlankScreen88200724Navigator },
BlankScreen87200723: { screen: BlankScreen87200723Navigator },
BlankScreen86200722: { screen: BlankScreen86200722Navigator },
BlankScreen85200707: { screen: BlankScreen85200707Navigator },
BlankScreen84200706: { screen: BlankScreen84200706Navigator },
BlankScreen83200703: { screen: BlankScreen83200703Navigator },
BlankScreen82200702: { screen: BlankScreen82200702Navigator },
BlankScreen81200701: { screen: BlankScreen81200701Navigator },
BlankScreen80200700: { screen: BlankScreen80200700Navigator },
BlankScreen79200699: { screen: BlankScreen79200699Navigator },
BlankScreen78200698: { screen: BlankScreen78200698Navigator },
BlankScreen77200697: { screen: BlankScreen77200697Navigator },
BlankScreen76200696: { screen: BlankScreen76200696Navigator },
BlankScreen74200694: { screen: BlankScreen74200694Navigator },
CopyOfCopyOfBlankScreen34200693: { screen: CopyOfCopyOfBlankScreen34200693Navigator },
CopyOfCopyOfBlankScreen34200692: { screen: CopyOfCopyOfBlankScreen34200692Navigator },
CopyOfCopyOfBlankScreen34200691: { screen: CopyOfCopyOfBlankScreen34200691Navigator },
CopyOfCopyOfBlankScreen34200690: { screen: CopyOfCopyOfBlankScreen34200690Navigator },
BlankScreen69200688: { screen: BlankScreen69200688Navigator },
BlankScreen68200687: { screen: BlankScreen68200687Navigator },
BlankScreen67200686: { screen: BlankScreen67200686Navigator },
BlankScreen66200685: { screen: BlankScreen66200685Navigator },
BlankScreen65200684: { screen: BlankScreen65200684Navigator },
BlankScreen64200683: { screen: BlankScreen64200683Navigator },
CopyOfBlankScreen34200682: { screen: CopyOfBlankScreen34200682Navigator },
CopyOfBlankScreen34200681: { screen: CopyOfBlankScreen34200681Navigator },
CopyOfBlankScreen34200680: { screen: CopyOfBlankScreen34200680Navigator },
CopyOfBlankScreen34200679: { screen: CopyOfBlankScreen34200679Navigator },
CopyOfBlankScreen34200678: { screen: CopyOfBlankScreen34200678Navigator },
CopyOfBlankScreen34200677: { screen: CopyOfBlankScreen34200677Navigator },
CopyOfBlankScreen34200676: { screen: CopyOfBlankScreen34200676Navigator },
CopyOfBlankScreen34200675: { screen: CopyOfBlankScreen34200675Navigator },
CopyOfBlankScreen34200674: { screen: CopyOfBlankScreen34200674Navigator },
CopyOfBlankScreen34200673: { screen: CopyOfBlankScreen34200673Navigator },
CopyOfBlankScreen34200672: { screen: CopyOfBlankScreen34200672Navigator },
CopyOfBlankScreen34200671: { screen: CopyOfBlankScreen34200671Navigator },
CopyOfBlankScreen34200670: { screen: CopyOfBlankScreen34200670Navigator },
CopyOfBlankScreen34200669: { screen: CopyOfBlankScreen34200669Navigator },
CopyOfBlankScreen34200668: { screen: CopyOfBlankScreen34200668Navigator },
CopyOfBlankScreen34200667: { screen: CopyOfBlankScreen34200667Navigator },
CopyOfBlankScreen34200666: { screen: CopyOfBlankScreen34200666Navigator },
CopyOfBlankScreen34200665: { screen: CopyOfBlankScreen34200665Navigator },
CopyOfBlankScreen34200664: { screen: CopyOfBlankScreen34200664Navigator },
CopyOfBlankScreen34200663: { screen: CopyOfBlankScreen34200663Navigator },
CopyOfBlankScreen34200662: { screen: CopyOfBlankScreen34200662Navigator },
CopyOfBlankScreen34200661: { screen: CopyOfBlankScreen34200661Navigator },
CopyOfBlankScreen34200660: { screen: CopyOfBlankScreen34200660Navigator },
CopyOfBlankScreen34200659: { screen: CopyOfBlankScreen34200659Navigator },
CopyOfBlankScreen34200658: { screen: CopyOfBlankScreen34200658Navigator },
CopyOfBlankScreen34200657: { screen: CopyOfBlankScreen34200657Navigator },
CopyOfBlankScreen34200656: { screen: CopyOfBlankScreen34200656Navigator },
CopyOfBlankScreen34200655: { screen: CopyOfBlankScreen34200655Navigator },
CopyOfBlankScreen34200654: { screen: CopyOfBlankScreen34200654Navigator },
CopyOfBlankScreen34200653: { screen: CopyOfBlankScreen34200653Navigator },
CopyOfBlankScreen34200652: { screen: CopyOfBlankScreen34200652Navigator },
BlankScreen34200651: { screen: BlankScreen34200651Navigator },
BlankScreen33200636: { screen: BlankScreen33200636Navigator },
BlankScreen32200635: { screen: BlankScreen32200635Navigator },
BlankScreen31200634: { screen: BlankScreen31200634Navigator },
BlankScreen30200633: { screen: BlankScreen30200633Navigator },
BlankScreen29200632: { screen: BlankScreen29200632Navigator },
BlankScreen28200614: { screen: BlankScreen28200614Navigator },
BlankScreen27200542: { screen: BlankScreen27200542Navigator },
BlankScreen24200539: { screen: BlankScreen24200539Navigator },
BlankScreen23200489: { screen: BlankScreen23200489Navigator },
BlankScreen22200488: { screen: BlankScreen22200488Navigator },
BlankScreen20200351: { screen: BlankScreen20200351Navigator },
BlankScreen19200350: { screen: BlankScreen19200350Navigator },
BlankScreen18200326: { screen: BlankScreen18200326Navigator },
BlankScreen17200323: { screen: BlankScreen17200323Navigator },
BlankScreen16200317: { screen: BlankScreen16200317Navigator },
BlankScreen15200312: { screen: BlankScreen15200312Navigator },
BlankScreen13200310: { screen: BlankScreen13200310Navigator },
BlankScreen12200309: { screen: BlankScreen12200309Navigator },
BlankScreen11200308: { screen: BlankScreen11200308Navigator },
BlankScreen10200307: { screen: BlankScreen10200307Navigator },
BlankScreen9200306: { screen: BlankScreen9200306Navigator },
BlankScreen8200305: { screen: BlankScreen8200305Navigator },
BlankScreen7200304: { screen: BlankScreen7200304Navigator },
BlankScreen6200303: { screen: BlankScreen6200303Navigator },
BlankScreen5200302: { screen: BlankScreen5200302Navigator },
BlankScreen4200301: { screen: BlankScreen4200301Navigator },
BlankScreen3200300: { screen: BlankScreen3200300Navigator },
BlankScreen2200299: { screen: BlankScreen2200299Navigator },
BlankScreen1200298: { screen: BlankScreen1200298Navigator },
BlankScreen0200297: { screen: BlankScreen0200297Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
